# Provenance Guard

> ### 👋 Start here
>
> **New to this repo? Read [RUNNING.md](RUNNING.md) first.**
>
> Once `python test.py` passes, in one terminal:
>
> ```bash
> python app.py
> ```
>
> and in another:
>
> ```bash
> curl -X POST http://127.0.0.1:5000/ping \
>   -H "Content-Type: application/json" \
>   -d '{"message": "hello"}'
> ```
>
> That's a web service. Something sent it text and it sent something back.
> Everything this unit is filling in the middle.
>
> **The rest of this file is your submission.** Fill it in as you go.

---

<!-- ─────────────────────────────────────────────────────────────────────────
     Unit 7 asks for the first five sections. Unit 8 adds the five below.

     Everything is pasted as TEXT. A pasted curl response gets full credit;
     a picture of your terminal gets none.
     ───────────────────────────────────────────────────────────────────────── -->

<!-- ═══════════════════════ UNIT 7 — THE BUILD ═══════════════════════ -->

## What This Does

<!-- The path a submission takes, from arriving to the label a reader sees.
     Six or seven steps — this is the trace you wrote in Milestone 1. -->

1. **A writer sends their text.** `POST /submit` arrives with JSON:
   `{"text": "...", "creator_id": "..."}`.
2. **The route checks the input before anything else runs.** If `text` is
   missing, not a string, empty, or far too long, the service answers `400`
   with a plain error and writes a `rejected` entry to the audit log. No model
   runs on a bad request.
3. **Signal one reads how predictable the text is.** `detector.model_signal`
   runs gpt2 on this machine and measures perplexity — how surprised the model
   is by each next word — then squashes it onto 0–1. Higher means more
   predictable, which this service treats as more AI-like.
4. **Signal two measures the shape of the text.** `stylometry.style_signal`
   looks at how much sentence lengths vary, how much vocabulary repeats, and
   how punctuation is used, and turns that into a second 0–1 score in the same
   direction. It never reads what the text says.
5. **The two scores become one.** `scoring.combine_signals` merges them into a
   single 0–1 score.
6. **The score becomes words.** `scoring.score_to_label` places the score in
   one of three bands — high-confidence human, unsure, high-confidence AI — and
   picks the sentence a reader will see.
7. **The decision is logged and returned.** The service gives the submission a
   `content_id`, writes the decision to `logs/audit.jsonl` with both signal
   scores, the combined score, the label and status `decided`, and returns the
   same fields to the writer. If the writer thinks it's wrong, they send that
   `content_id` with their reasoning to `POST /appeal`. That adds an entry
   that moves the item to `under_review`, without erasing the original
   decision.

**The person I followed through it:** someone writing in their second
language, using short sentences and words they're sure of. At step 3 their
text is very predictable, so signal one scores it close to machine writing.
At step 4 their sentences may be fairly even and their vocabulary narrow,
which pushes signal two the same way. Both signals lean "AI" for reasons that
have nothing to do with who wrote it. That makes the decision at steps 5 and 6
the one that matters: **I would rather miss AI text than accuse this writer**,
so the combining rule and the bands should leave a wide "unsure" zone, and the
"high-confidence AI" label should need both signals to agree.


---

## Signals and Scoring

<!-- For each signal: what property it measures, why that might differ between
     human and AI writing, and WHAT IT CAN'T SEE.

     The blind spot is not optional. If you can't name it you don't understand
     the signal yet — and unit 8's attack set is built out of blind spots. -->

### Signal one — the model signal

**What it measures:** How predictable the text is to gpt2, running locally.
`detector.model_signal` computes perplexity (how surprised the model is by
each next word, on average) and maps it onto 0–1 with a logistic curve:
perplexity 45 scores 0.5, and lower perplexity scores higher. **Higher means
more likely AI.** I left the midpoint at 45. On my calibration inputs, AI
text scored perplexity ~15 and the human paragraphs ~50, so 45 already sits
between them.

**Why that might differ between human and AI writing:** A language model
writes by repeatedly picking a likely next word, so its output is text a
model finds easy to predict. People make odder choices: a specific word over
the typical one, a sentence that turns halfway through.

**What it can't see:** Predictability isn't authorship. The signal rewards
common words in short, ordinary sentences, so plain human writing — a
second-language writer, a younger writer, anyone writing simply on purpose —
scores almost as machine-like as machine writing. It also misses the other
direction: AI text full of rare or ornate words can look human, because rare
words are what gpt2 fails to predict.

### Signal two — the style signal

**What it measures:** The shape of the text, from three measures in
`stylometry.py`:

| Measure | How it's computed | Direction | Weight |
|---|---|---|---|
| Sentence-length spread | stdev ÷ mean of words per sentence | higher = more human | 0.6 |
| Type-token ratio | unique ÷ total words, averaged over 50-word windows | higher = more human | 0.1 |
| Punctuation density | commas, semicolons, dashes, brackets, quotes, `?` and `!` per word | higher = more human | 0.3 |

Each measure is scaled onto 0–1 between an AI-ish and a human-ish reference
value (spread 0.15→0.70, TTR 0.60→0.85, punctuation 0.04→0.15). The weighted
average is then flipped, so **higher means more likely AI**, the same
direction as signal one. A one-sentence submission has no spread, so that
measure drops out and the other two carry the score.

The weights come from calibration. Spread separated the inputs cleanly (AI
0.10–0.17, human 0.70–0.74). Type-token ratio pointed the *wrong* way on
paragraph-length text: the AI paragraphs had the most varied vocabulary
(0.90–0.93). So it stays in, because the brief names it, but at a weight
where it can't drag the score backwards.

**Why that might differ between human and AI writing:** "Most likely next
word" produces even, mid-length sentences and tidy punctuation on average.
Human writing is lumpier — a one-word sentence next to a long one, a dash
or a semicolon where it feels right.

**What it can't see:** Meaning. It measures the shape of the text and nothing
else, so anything that changes the shape without changing the substance moves
it: added typos, sentences chopped in half, a pasted quotation, a few
deliberately odd punctuation marks. AI text with those edits looks more human
to this signal, and it costs the person editing almost nothing.

### The combining rule

<!-- Write the rule in words, then give the numbers. What happens when the two
     signals disagree? -->

**The rule:** Average the two signals equally. To be called high-confidence
AI, though, *both* signals have to lean AI on their own. If either one reads
more human than the agreement floor, the score is capped just below the AI
threshold, so disagreement can produce "unsure" but never an accusation.
Calling something human needs no such agreement, because a wrong "human"
costs far less than a wrong "AI".

**The numbers:** `WEIGHT_MODEL_SIGNAL = 0.5`, `WEIGHT_STYLE_SIGNAL = 0.5`,
`AGREEMENT_FLOOR = 0.6`. If `min(model, style) < 0.6`, the score is capped at
`AI_THRESHOLD − 0.01 = 0.64`. All four are in `config.py`.

**Where it lives:** `scoring.py::combine_signals`

<!-- ⚠️ The grader checks your code against that line. If your rule lives
     somewhere else, say where. -->

**A case where my two signals split, and what my rule does with it:**

My "lightly edited AI" calibration input was an AI paragraph I loosened by
hand: contractions, a dash, shorter words. Signal one read it as
**0.507**, because the edits made it less predictable. Signal two read it as
**0.821**, because the sentences still marched in step (spread 0.10). The plain
average is 0.664, just over the AI threshold. My rule sees that the model
signal is below 0.6 and caps it at **0.64 → unsure**. Here that's a miss,
because the text really was AI. But it's the right kind of miss: the same rule
stops a human whose sentences just happen to be even from being accused on
one signal alone.



---

## Label Variants

<!-- The exact text of all three labels, as a reader would see them, and the
     score range each covers.

     Write them for someone who has never heard the word "threshold". -->

| Label | Score range | The exact text a reader sees |
|---|---|---|
| high-confidence human | 0.00 – 0.35 | We think this was written by a person. |
| unsure | 0.35 – 0.65 | We can't tell whether this was written by a person or with AI help. That's common for plain or short writing, and it isn't an accusation. If you wrote this yourself and want a person to look at it, you can appeal. |
| high-confidence AI | 0.65 – 1.00 | Our checks suggest this was likely written with AI. They can be wrong — especially for simple, clear writing — so if you wrote this yourself, please appeal and a person will review it. |

All three are reachable. On the calibration inputs, the casual human
paragraph scored 0.262 (human), the lightly edited AI 0.640 (unsure) and the
clearly AI paragraph 0.843 (AI).

**Why I worded the "unsure" one this way:**
<!-- It's the hardest of the three. It has to admit uncertainty without
     sounding like an accusation, because the person reading it may well have
     written every word themselves. -->

The person most likely to see "unsure" wrote every word themselves: plain
writing lands here often. So the label says outright that it **isn't an
accusation**, and it gives a reason that points at the writing style, not
the writer's honesty ("common for plain or short writing"). It offers the
appeal as an option, not a demand. I left out any score or percentage,
because "52% AI" reads as "probably cheated" to anyone who doesn't know what
a threshold is. The AI label also admits it can be wrong and names the case
where it most often is, because the writer reading it may be that case.



---

## Sample Run

<!-- One submission and one appeal, pasted as text: the request, the response,
     and the log entries. -->

**A submission**

<!-- The response needs content_id, guess, confidence, label, AND both
     signal scores - model_score and style_score. Unit 8's tools read those
     two off the response, so leaving them out costs you next unit's
     diagnostics. -->

This is the case Milestone 1 traced: a plainly written human paragraph, the
kind a second-language writer produces. Both signals call it AI, so the
agreement rule can't save it, and it gets the high-confidence AI label. That
is a false positive, and the appeal is what stands between this writer and
the label.

```bash
$ curl -X POST http://127.0.0.1:5000/submit \
  -H "Content-Type: application/json" \
  -d '{"text": "I moved to this city two years ago. At first it was hard for me. I did not know anyone and my English was not good. I worked in a restaurant in the kitchen. The work was long but the people were kind. On my free day I went to the library to study. Now I can talk with my neighbors and I have some friends. I am proud of this.", "creator_id": "steven"}'
```

```json
{
    "combined_score": 0.8236,
    "confidence": 0.496,
    "content_id": "cb0a0967-9811-4cbd-b9cf-0082a80c91f1",
    "guess": "ai",
    "label": "Our checks suggest this was likely written with AI. They can be wrong — especially for simple, clear writing — so if you wrote this yourself, please appeal and a person will review it.",
    "model_score": 0.8339,
    "status": "decided",
    "style_score": 0.8133
}
```

**An appeal**

```bash
$ curl -X POST http://127.0.0.1:5000/appeal \
  -H "Content-Type: application/json" \
  -d '{"content_id": "cb0a0967-9811-4cbd-b9cf-0082a80c91f1", "reasoning": "I wrote this myself about my first two years here. I use simple words because English is my second language."}'
```

```json
{
    "content_id": "cb0a0967-9811-4cbd-b9cf-0082a80c91f1",
    "message": "Thanks — your appeal is recorded and a person will review this decision. The original label stays on record until then.",
    "status": "under_review"
}
```

**What the log shows afterwards**

```bash
$ curl "http://127.0.0.1:5000/log?limit=3"
```

```json
{
    "count": 2,
    "entries": [
        {
            "combined_score": 0.8236,
            "confidence": 0.496,
            "content_id": "cb0a0967-9811-4cbd-b9cf-0082a80c91f1",
            "creator_id": "steven",
            "guess": "ai",
            "label": "Our checks suggest this was likely written with AI. They can be wrong — especially for simple, clear writing — so if you wrote this yourself, please appeal and a person will review it.",
            "model_score": 0.8339,
            "status": "decided",
            "style_score": 0.8133,
            "timestamp": "2026-11-01T22:50:27+00:00"
        },
        {
            "content_id": "cb0a0967-9811-4cbd-b9cf-0082a80c91f1",
            "creator_id": "steven",
            "event": "appeal",
            "reasoning": "I wrote this myself about my first two years here. I use simple words because English is my second language.",
            "status": "under_review",
            "timestamp": "2026-11-01T22:50:27+00:00"
        }
    ]
}
```

The original decision stays in the log, and the appeal sits after it,
moving the item to `under_review`. `confidence` is how far the score sits
inside its label band, scaled to 0–1. It isn't a probability, and "unsure"
always reports 0.

---

## How I Used AI

**Moment 1**

- *What I asked for:* I asked Claude Code to do Milestones 1 and 2: the
  trace of a submission and my five acceptance criteria.
- *What came back:* A seven-step trace that follows a second-language writer
  through the service, the blind spot for each signal, and five criteria:
  no false positives on my own writing, plain writing not flagged, clear
  cases separating by 0.30, every appeal recorded, and bad input refused
  without a crash. It pointed out that the criteria committed me to building
  a `400`/`413` for bad input and a `404` for unknown appeals.
- *What I changed:* <!-- TODO (Steven): what you actually changed or decided
  after reading it. If you changed nothing, say so honestly. -->

**Moment 2**

- *What I asked for:* I asked Claude Code to build Milestones 3–5: the
  route, signal two, the combining rule, the labels and the appeal.
- *What came back:* Working code plus a calibration run on five inputs. The
  calibration showed type-token ratio points the wrong way on short text, so
  it got weight 0.1. It also showed that a plainly written human paragraph
  scores as AI on both signals. Claude kept that false positive visible and
  used it as the sample run, rather than tuning thresholds to hide it.
- *What I changed:* <!-- TODO (Steven): what you changed, checked or pushed
  back on. Note that every "human" sample here was written by Claude or taken
  from Mark Twain, not by me — criterion 1 still needs ten pieces I wrote. -->

<!-- ═══════════════════════ UNIT 8 — THE TEST ═══════════════════════ -->

---

## Rate Limiting

**My limits:** 10 per minute, 200 per day

**Why those numbers and not others:**
For a genuine writer submitting work for analysis, 10 submissions per minute (one every 6 seconds) is far higher than normal human writing or editing speed, and 200 per day provides plenty of headroom for active drafting and appeals across a full workday without friction. Conversely, for an adversary or automated script attempting to probe decision boundaries, map detector thresholds, or brute-force variations, 10/minute dramatically slows down automated exploration, and 200/day cuts probing off entirely before meaningful boundary mapping can occur.

**What a caller counts as:**
A caller is counted primarily by `creator_id` provided in the JSON payload, falling back to the client IP address (`get_remote_address()`) if `creator_id` is omitted, empty, or not a string. Per-creator tracking prevents an attacker from evading limits simply by routing requests through a shared proxy or VPN, while IP fallback prevents an unauthenticated attacker from circumventing limits by inventing random creator IDs.

**The run of status codes when I pushed past it:**

<!-- python run_attacks.py --flood 15 -->

```
200 200 200 200 200 200 200 200 200 200 429 429 429 429 429
```

---

## Attack Run — Before

<!-- Every attack with its outcome and a held-or-broke mark.
     `run_attacks.py --label before` produces the table. -->



**Ten audit log entries from the run**

<!-- Choose entries that show the interesting failures, not the ten easiest. -->

```json

```

**The single worst outcome** — the one I'd least want to explain to a writer
whose work got caught by it:



---

## Run Log and Verdicts

<!-- Your five criteria across three trials. `run_eval.py --label before`. -->

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1.  |  |  |  |  |  |
| 2.  |  |  |  |  |  |
| 3.  |  |  |  |  |  |
| 4.  |  |  |  |  |  |
| 5.  |  |  |  |  |  |

**Real output from one trial**, pasted as text, naming the file and function
that produced it:

```json

```

**Diagnoses**

<!-- For each miss AND each broken attack: the stage and the mechanism.

     Your service has five stages: the route, signal one, signal two, the
     combining rule, and the label mapping.

     Not a diagnosis:  "The evasion attacks got through."
     A diagnosis:      "Four evasion inputs got through. All four had typos
                        added to AI-generated text. My second signal measures
                        word variety, and typos raise word variety — so it read
                        them as more human. My combining rule weights that
                        signal at 0.6, so it dragged the whole score down."

     Look for a pattern. Five failures on one signal is one problem, not five. -->



---

## The Improvement

**What I changed:**

**Which diagnosis pointed at it:**

### Attack Run — After

<!-- Same format. `run_attacks.py --label after` -->



**Did it help, and how do I know:**

<!-- Widening the unsure band usually fixes one problem and creates another.
     Reporting that trade honestly is worth full credit. -->



---

## What's Still Broken

<!-- For each attack still getting through and each criterion still missed:
     what you'd do, and why you stopped. -->



**The trade I'd make if this ran for real:**

<!-- Two sentences. Fewer wrong accusations means more AI text getting through.
     Say which way you'd go and WHO PAYS FOR IT. -->



<!-- ═════════════════════════════════════════════════════════════════════

     SUBMISSION CHECKLIST — unit 7

       [ ] criteria.md has five numbered criteria, each naming a target
       [ ] Each has a reason underneath
       [ ] POST /submit returns content_id, guess, confidence, label,
           model_score and style_score
       [ ] Two signals that measure DIFFERENT things, each with a named blind spot
       [ ] Three label variants, all reachable, written out in full
       [ ] POST /appeal changes status and writes to the log
       [ ] Signals and Scoring names scoring.py::combine_signals
       [ ] Sample Run: a submission AND an appeal, as pasted text
       [ ] At least four new commits
       [ ] Repository URL submitted — WRITE IT DOWN

     SUBMISSION CHECKLIST — unit 8

       [x] Rate limiting on /submit, with your numbers justified
       [x] The pasted run of status codes showing 429
       [x] Audit log with all nine fields, recording rejections too
       [ ] The attack set run IN FULL, every input with an outcome
       [ ] Ten audit log entries pasted as text
       [ ] Five criteria across three trials
       [ ] A diagnosis for every miss and every broken attack — stage AND mechanism
       [ ] One improvement, with Attack Run — After
       [ ] What's Still Broken, including the production trade
       [ ] At least four new commits
       [ ] The SAME repository URL as last unit

     Do not delete and recreate this repository.
     ═════════════════════════════════════════════════════════════════════ -->

---

📖 **How to run this project: [RUNNING.md](RUNNING.md)**
