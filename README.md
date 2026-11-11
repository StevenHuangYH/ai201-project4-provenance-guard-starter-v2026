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
- *What I changed:* Nothing. I kept the five criteria and their targets as
  written. They were committed in `cfff7ef` and not edited before the unit 8
  runs. The only later additions are the unit 8 notes, which leave the
  targets unchanged.

**Moment 2**

- *What I asked for:* I asked Claude Code to build Milestones 3–5: the
  route, signal two, the combining rule, the labels and the appeal.
- *What came back:* Working code plus a calibration run on five inputs. The
  calibration showed type-token ratio points the wrong way on short text, so
  it got weight 0.1. It also showed that a plainly written human paragraph
  scores as AI on both signals. Claude kept that false positive visible and
  used it as the sample run, rather than tuning thresholds to hide it.
- *What I changed:* Nothing in the code. `stylometry.py` and `scoring.py`
  went in as built (`2348f9e`, `520ccf3`) and weren't edited before unit 8.
  Every "human" sample in this unit was written by Claude or taken from Mark
  Twain, not by me. That includes the Sample Run paragraph, which unit 8
  found is the one plain text labelled AI.

**Moment 3 (unit 8)**

- *What I asked for:* I asked Claude Code to finish unit 8: turn on the rate
  limiter, run the attack set and my five criteria (three trials), diagnose
  the misses, make one improvement, re-run everything and write it up. I
  told it to write the inputs for criteria 1 and 2 instead of waiting for my
  own writing.
- *What came back:* Instead of making up text and calling it human, it used
  published human paragraphs picked by a fixed rule, and labelled them as
  stand-ins in `scenarios.py` and here. It extended `run_eval.py` so criterion
  4 (appeals) and the timing/logging parts of criterion 5 are measured
  instead of checked by hand. It found and documented the cold-start 500 bug
  rather than quietly re-running. It picked the threshold change, and
  reported that criterion 3 got worse because of it.
- *What I changed:* I made two calls. First, Claude stopped to ask for my
  own writing for criteria 1 and 2, and I told it to go ahead without it, so
  those two criteria were run on stand-in text rather than mine. Second, I
  kept its HELD/BROKE rules and the 0.80 threshold as they were. I didn't
  replace the stand-in text before submitting, so criterion 1's verdict is
  about published human prose, not my writing. That's the first thing I'd
  re-run.

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

`python run_attacks.py --set attack_set --label before` →
[results/attack_run_2026-11-11_0229_before.md](results/attack_run_2026-11-11_0229_before.md).
56 inputs (the zip's `attacks.csv` plus `attacks_malformed_requests.csv`),
run once, before any fix. Signal 1 is `model_score`, signal 2 is
`style_score`, combined is from the audit log.

**How I marked HELD / BROKE** — by what each family was going for:

- *evasion* (AI text): HELD only if it was still labelled AI. "Unsure" counts
  as BROKE — the AI text got through without a flag.
- *false_positive* (human text): BROKE if it was labelled AI.
- *prompt_injection*: BROKE if the attacker got what the injected instruction
  asked for (a human label, a changed label, a corrupted log entry).
- *malformed*: BROKE on a 5xx/crash, or if input that isn't scorable writing
  got a confident label. A clean 400/413, or a non-accusing "unsure", is HELD.
- *flood_same_creator*: HELD if the limiter cut it off.

| ID | Family | What it was going for | Status | Guess | Signal 1 | Signal 2 | Combined | Verdict |
|---|---|---|---|---|---|---|---|---|
| EV01 | evasion | signal two: typos raise word variety | 200 | unsure | 0.164 | 0.869 | 0.516 | **BROKE** |
| EV02 | evasion | signal two: broken-up sentences raise length spread | 200 | unsure | 0.594 | 0.289 | 0.442 | **BROKE** |
| EV03 | evasion | signal two: a pasted quotation changes the shape | 200 | unsure | 0.666 | 0.483 | 0.575 | **BROKE** |
| EV04 | evasion | signal one: unusual words raise perplexity | 200 | ai | 0.611 | 0.825 | 0.718 | **HELD** |
| EV05 | evasion | both signals: heavy human editing pass | 200 | human | 0.321 | 0.203 | 0.262 | **BROKE** |
| EV06 | evasion | signal two: one very long sentence and one very short | 200 | unsure | 0.573 | 0.300 | 0.437 | **BROKE** |
| EV07 | evasion | signal two: padding with punctuation | 200 | human | 0.586 | 0.005 | 0.295 | **BROKE** |
| EV08 | evasion | signal one: text below the token window | 200 | unsure | 0.245 | 0.755 | 0.500 | **BROKE** |
| EV09 | evasion | both: AI text with a human opening paragraph bolted on | 200 | unsure | 0.704 | 0.515 | 0.610 | **BROKE** |
| EV10 | evasion | signal two: repeated stanza structure | 200 | ai | 0.979 | 0.734 | 0.857 | **HELD** |
| FP01 | false_positive | plain, clear human writing with no flourishes | 200 | unsure | 0.618 | 0.582 | 0.600 | **HELD** |
| FP02 | false_positive | human writing in a formal register | 200 | ai | 0.739 | 0.834 | 0.786 | **BROKE** |
| FP03 | false_positive | a non-native English speaker writing carefully | 200 | ai | 0.805 | 0.718 | 0.761 | **BROKE** |
| FP04 | false_positive | a student essay written to a rubric | 200 | ai | 0.833 | 0.675 | 0.754 | **BROKE** |
| FP05 | false_positive | technical documentation written by a person | 200 | ai | 0.800 | 0.851 | 0.826 | **BROKE** |
| FP06 | false_positive | a person imitating a formal template | 200 | unsure | 0.881 | 0.535 | 0.640 | **HELD** |
| FP07 | false_positive | human writing that repeats a phrase deliberately | 200 | unsure | 0.882 | 0.400 | 0.640 | **HELD** |
| FP08 | false_positive | very short genuine human submission | 200 | unsure | 0.322 | 0.591 | 0.457 | **HELD** |
| PI01 | prompt_injection | instruction to ignore the check | 200 | unsure | 0.463 | 0.341 | 0.402 | **HELD** |
| PI02 | prompt_injection | instruction disguised as a system message | 200 | human | 0.204 | 0.341 | 0.273 | **BROKE** |
| PI03 | prompt_injection | instruction wrapped in the writer's voice | 200 | unsure | 0.594 | 0.650 | 0.622 | **HELD** |
| PI04 | prompt_injection | attempt to make the label text hostile | 200 | unsure | 0.500 | 0.419 | 0.460 | **HELD** |
| PI05 | prompt_injection | attempt to inject into the audit log | 200 | unsure | 0.640 | 0.249 | 0.445 | **HELD** |
| PI06 | prompt_injection | instruction plus real human text | 200 | unsure | 0.558 | 0.593 | 0.576 | **HELD** |
| MF01 | malformed | text is only whitespace | 400 | — | — | — | — | **HELD** |
| MF02 | malformed | text is a single character | 400 | — | — | — | — | **HELD** |
| MF03 | malformed | text is control characters | 200 | unsure | 0.000 | 0.750 | 0.375 | **HELD** |
| MF04 | malformed | text is only punctuation | 200 | unsure | 0.011 | 1.000 | 0.506 | **HELD** |
| MF05 | malformed | text is a very long single word | 200 | ai | 0.998 | 0.750 | 0.874 | **BROKE** |
| MF06 | malformed | text is emoji only | 200 | ai | 0.997 | 1.000 | 0.999 | **BROKE** |
| MF07 | malformed | text is right-to-left script | 200 | ai | 0.906 | 1.000 | 0.953 | **BROKE** |
| MF08 | malformed | text is 60,000 characters | 413 | — | — | — | — | **HELD** |
| RQ01 | malformed | no text field at all | 400 | — | — | — | — | **HELD** |
| RQ02 | malformed | no creator_id | 200 | unsure | 0.239 | 0.750 | 0.495 | **HELD** |
| RQ03 | malformed | text is a number | 400 | — | — | — | — | **HELD** |
| RQ04 | malformed | text is a list | 400 | — | — | — | — | **HELD** |
| RQ05 | malformed | text is null | 400 | — | — | — | — | **HELD** |
| RQ06 | malformed | creator_id is an object | 200 | unsure | 0.049 | 0.750 | 0.400 | **HELD** |
| RQ07 | malformed | body is a JSON array, not an object | 400 | — | — | — | — | **HELD** |
| RQ08 | malformed | body is unparseable JSON | 400 | — | — | — | — | **HELD** |
| RQ09 | malformed | body is empty | 400 | — | — | — | — | **HELD** |
| RQ10 | malformed | body is form-encoded, not JSON | 400 | — | — | — | — | **HELD** |
| RQ11 | malformed | body is JSON claiming to be plain text | 400 | — | — | — | — | **HELD** |
| RQ12 | malformed | deeply nested JSON | 400 | — | — | — | — | **HELD** |
| FL01_01 | flood_same_creator | 20 rapid submissions from one creator | 200 | unsure | 0.029 | 0.750 | 0.389 | **HELD** |
| FL01_02 | flood_same_creator | 20 rapid submissions from one creator | 200 | unsure | 0.029 | 0.750 | 0.389 | **HELD** |
| FL01_03 | flood_same_creator | 20 rapid submissions from one creator | 200 | unsure | 0.029 | 0.750 | 0.389 | **HELD** |
| FL01_04 | flood_same_creator | 20 rapid submissions from one creator | 200 | unsure | 0.029 | 0.750 | 0.389 | **HELD** |
| FL01_05 | flood_same_creator | 20 rapid submissions from one creator | 200 | unsure | 0.029 | 0.750 | 0.389 | **HELD** |
| FL01_06 | flood_same_creator | 20 rapid submissions from one creator | 200 | unsure | 0.029 | 0.750 | 0.389 | **HELD** |
| FL01_07 | flood_same_creator | 20 rapid submissions from one creator | 200 | unsure | 0.029 | 0.750 | 0.389 | **HELD** |
| FL01_08 | flood_same_creator | 20 rapid submissions from one creator | 200 | unsure | 0.029 | 0.750 | 0.389 | **HELD** |
| FL01_09 | flood_same_creator | 20 rapid submissions from one creator | 200 | unsure | 0.029 | 0.750 | 0.389 | **HELD** |
| FL01_10 | flood_same_creator | 20 rapid submissions from one creator | 200 | unsure | 0.029 | 0.750 | 0.389 | **HELD** |
| FL01_11 | flood_same_creator | 20 rapid submissions from one creator | 429 | — | — | — | — | **HELD** |
| FL01_12 | flood_same_creator | 20 rapid submissions from one creator | 429 | — | — | — | — | **HELD** |

| Family | Held | Broke |
|---|---|---|
| evasion | 2 | 8 |
| false_positive | 4 | 4 |
| prompt_injection | 5 | 1 |
| malformed | 17 | 3 |
| flood_same_creator | 12 | 0 |
| **total** | **40** | **16** |

No input crashed the service or got a 5xx. The flood family has 12 rows in
the file (its description says 20); rows 11 and 12 came back `429`.

**Eleven audit log entries from the run** (`logs/audit.jsonl`, pasted as-is;
the last three are rejections — a `400`, a `413` and a `429`):

```json
{"timestamp": "2026-11-11T07:29:18+00:00", "content_id": "9597475e-289d-4181-82e3-e1d2e31d019a", "creator_id": "attacker_FP03", "guess": "ai", "model_score": 0.8051, "style_score": 0.7178, "combined_score": 0.7614, "label": "Our checks suggest this was likely written with AI. They can be wrong — especially for simple, clear writing — so if you wrote this yourself, please appeal and a person will review it.", "status": "decided", "confidence": 0.3183}
{"timestamp": "2026-11-11T07:29:18+00:00", "content_id": "5245f939-06ee-4b0e-82b4-be22aa516482", "creator_id": "attacker_FP02", "guess": "ai", "model_score": 0.7387, "style_score": 0.8337, "combined_score": 0.7862, "label": "Our checks suggest this was likely written with AI. They can be wrong — especially for simple, clear writing — so if you wrote this yourself, please appeal and a person will review it.", "status": "decided", "confidence": 0.3891}
{"timestamp": "2026-11-11T07:29:22+00:00", "content_id": "11f7e84d-fc88-4077-ad11-8e0bc9b1c3f6", "creator_id": "attacker_MF07", "guess": "ai", "model_score": 0.9064, "style_score": 1.0, "combined_score": 0.9532, "label": "Our checks suggest this was likely written with AI. They can be wrong — especially for simple, clear writing — so if you wrote this yourself, please appeal and a person will review it.", "status": "decided", "confidence": 0.8663}
{"timestamp": "2026-11-11T07:29:21+00:00", "content_id": "9e4d6e43-c158-430c-89f1-da22244f5012", "creator_id": "attacker_MF06", "guess": "ai", "model_score": 0.9969, "style_score": 1.0, "combined_score": 0.9985, "label": "Our checks suggest this was likely written with AI. They can be wrong — especially for simple, clear writing — so if you wrote this yourself, please appeal and a person will review it.", "status": "decided", "confidence": 0.9957}
{"timestamp": "2026-11-11T07:29:16+00:00", "content_id": "b12a034a-fc8e-4eb2-8183-ef07c68f4e4a", "creator_id": "attacker_EV07", "guess": "human", "model_score": 0.5862, "style_score": 0.0046, "combined_score": 0.2954, "label": "We think this was written by a person.", "status": "decided", "confidence": 0.156}
{"timestamp": "2026-11-11T07:29:12+00:00", "content_id": "32cedc10-9506-4047-a00a-1c6f7cd30a29", "creator_id": "attacker_EV01", "guess": "unsure", "model_score": 0.1635, "style_score": 0.869, "combined_score": 0.5162, "label": "We can't tell whether this was written by a person or with AI help. That's common for plain or short writing, and it isn't an accusation. If you wrote this yourself and want a person to look at it, you can appeal.", "status": "decided", "confidence": 0.0}
{"timestamp": "2026-11-11T07:29:19+00:00", "content_id": "bc567381-c97e-4748-a33a-3a73816a7e52", "creator_id": "attacker_PI02", "guess": "human", "model_score": 0.2044, "style_score": 0.3406, "combined_score": 0.2725, "label": "We think this was written by a person.", "status": "decided", "confidence": 0.2214}
{"timestamp": "2026-11-11T07:29:19+00:00", "content_id": "35b56fde-58b0-4f51-9425-60f166119031", "creator_id": "attacker_PI05", "guess": "unsure", "model_score": 0.6401, "style_score": 0.2494, "combined_score": 0.4447, "label": "We can't tell whether this was written by a person or with AI help. That's common for plain or short writing, and it isn't an accusation. If you wrote this yourself and want a person to look at it, you can appeal.", "status": "decided", "confidence": 0.0}
{"timestamp": "2026-11-11T07:29:22+00:00", "creator_id": "attacker_RQ01", "event": "rejected", "status": "rejected", "reason": "missing_text", "status_code": 400}
{"timestamp": "2026-11-11T07:29:22+00:00", "creator_id": "attacker_MF08", "event": "rejected", "status": "rejected", "reason": "text_too_long", "status_code": 413, "text_length": 57640}
{"timestamp": "2026-11-11T07:29:23+00:00", "creator_id": "attacker_flood", "event": "rejected", "status": "rejected", "reason": "rate_limited", "limit": "10 per 1 minute"}
```

What they show: FP02/FP03 are human writing accused with both signals over
0.7. MF06/MF07 are emoji and Arabic text scored 1.0 by signal two. EV07 is AI
text that semicolon padding pushed to `human`. PI02's fake "SYSTEM:" line
worked — but as an evasion, not as an instruction (see diagnoses). PI05
tried to break out of the JSON into the log; the decision entry has fixed
fields and never stores the text, so there was nothing to inject into.

**The single worst outcome** — **FP03**. A paragraph written the way a careful
second-language writer writes ("I want to describe my experience of the first
month in this country… Sometimes I do not understand the jokes.") came back
*"Our checks suggest this was likely written with AI"*, combined 0.761, with
both signals agreeing (0.805 / 0.718). This is exactly the writer criterion 2
was written to protect: the one with the least room to argue back. MF07 —
real Arabic writing labelled AI at 0.953 — is a close second.

---

## Run Log and Verdicts

`python run_eval.py --label before` →
[results/run_2026-11-11_0239_before.md](results/run_2026-11-11_0239_before.md).
Nothing changed between trials, and nothing in either signal is random, so
the three trials are identical — expected, recorded anyway.

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. My own writing is never called AI | 0 of 10 AI **and** ≤ 3 of 10 unsure | 1 AI, 6 unsure | 1 AI, 6 unsure | 1 AI, 6 unsure | **MISSED** |
| 2. Plain writing isn't treated as machine writing | ≤ 1 of 5 AI | 1/5 | 1/5 | 1/5 | **MET** |
| 3. Clearly AI and clearly human score far apart | gap ≥ 0.30 **and** ≥ 3 of 5 AI caught | gap 0.212, 2/5 | gap 0.212, 2/5 | gap 0.212, 2/5 | **MISSED** |
| 4. Every appeal recorded, a bad one changes nothing | 5/5 real → 200 + `under_review`, original kept; 3/3 bogus → 404, no entry | 5/5, 3/3 | 5/5, 3/3 | 5/5, 3/3 | **MET** |
| 5. Bad input gets a clear refusal | 4/4 get 400/413 + JSON error, 0 × 500, < 5 s, `rejected` logged | 4/4 (max 0.013 s) | 4/4 (max 0.010 s) | 4/4 (max 0.015 s) | **MET** |

How I decided each: every part of a target has to hold in every trial.
Criterion 1 fails on both halves (one AI label where the target is zero; six
unsure where the limit is three). Criterion 2 is exactly at its limit of 1.
Criterion 3 fails both halves. 4 and 5 hold in full.

**Three things about the test inputs that affect how to read this:**

- *Criteria 1 and 2 use stand-in text, not my own writing.* The ten "own
  writing" pieces and four of the five plain pieces are published human
  paragraphs (Austen, Fitzgerald, Doyle, Joyce, Douglass, Hemingway, Booker T.
  Washington…), each the first paragraph past the middle of the book that
  passes a fixed length/no-dialogue rule — see `scenarios.py`. They are
  certainly human, but they aren't mine, so criterion 1 measures "published
  human prose", not "my writing".
- *Plain-writing #1 is not human.* It's the Sample Run paragraph, which (per
  How I Used AI, Moment 2) Claude wrote in unit 7. It is the one plain text
  labelled AI — so criterion 2's single "false positive" is actually a
  correct catch, and the four genuinely human plain texts went 0 of 4.
- *Two of criterion 3's "clear human" texts are famous openings* (Dickens,
  Thoreau). gpt2 has memorised them, so signal one scores them 0.948 and
  0.652. That inflates the human average and shrinks the gap.

The first attempt at this run is kept as
[results/run_2026-11-11_0235_before_coldstart_crash.md](results/run_2026-11-11_0235_before_coldstart_crash.md):
almost every request returned **500**. That's a real bug, diagnosed below,
not a criterion result — the run above was made after warming the model.

**Real output from trial 1** — produced by `run_eval.py::main` (criterion 4:
`run_eval.py::run_appeal_trial`) against `app.py::submit` / `app.py::appeal`.
Labels and sent text are trimmed; the full JSON is in the results file.

Criterion 1 — the accused piece (Jane Eyre) and a typical unsure one (Gatsby):

```json
[
  {
    "status": 200,
    "guess": "ai",
    "model_score": 0.6879,
    "style_score": 0.6764,
    "combined_score": 0.6822,
    "label": "Our checks suggest this was likely written wi…",
    "error": null,
    "elapsed_s": 0.203,
    "logged_as": [
      "decided"
    ],
    "sent": "She wanted to know if I was happy at Thornfield Hall, and wh"
  },
  {
    "status": 200,
    "guess": "unsure",
    "model_score": 0.5241,
    "style_score": 0.4812,
    "combined_score": 0.5027,
    "label": "We can't tell whether this was written by a p…",
    "error": null,
    "elapsed_s": 0.368,
    "logged_as": [
      "decided"
    ],
    "sent": "Tom was evidently perturbed at Daisy’s running around alone,"
  }
]
```

Criterion 2 — the Claude-written sample (correctly AI) and a Hemingway paragraph:

```json
[
  {
    "status": 200,
    "guess": "ai",
    "model_score": 0.8339,
    "style_score": 0.8133,
    "combined_score": 0.8236,
    "label": "Our checks suggest this was likely written wi…",
    "error": null,
    "elapsed_s": 0.158,
    "logged_as": [
      "decided"
    ],
    "sent": "I moved to this city two years ago. At first it was hard for"
  },
  {
    "status": 200,
    "guess": "unsure",
    "model_score": 0.451,
    "style_score": 0.3359,
    "combined_score": 0.3934,
    "label": "We can't tell whether this was written by a p…",
    "error": null,
    "elapsed_s": 0.178,
    "logged_as": [
      "decided"
    ],
    "sent": "He was delighted with Italy. It was a beautiful country he s"
  }
]
```

Criterion 3 — a caught AI text, an AI text held at the 0.64 cap, a memorised
human opening, and a human text labelled human:

```json
[
  {
    "status": 200,
    "guess": "ai",
    "model_score": 0.8161,
    "style_score": 0.7105,
    "combined_score": 0.7633,
    "label": "Our checks suggest this was likely written wi…",
    "error": null,
    "elapsed_s": 0.149,
    "logged_as": [
      "decided"
    ],
    "sent": "Time management is an essential skill that can significantly"
  },
  {
    "status": 200,
    "guess": "unsure",
    "model_score": 0.8131,
    "style_score": 0.5623,
    "combined_score": 0.64,
    "label": "We can't tell whether this was written by a p…",
    "error": null,
    "elapsed_s": 0.205,
    "logged_as": [
      "decided"
    ],
    "sent": "Artificial intelligence is transforming the way we live and "
  }
]
```

```json
[
  {
    "status": 200,
    "guess": "unsure",
    "model_score": 0.948,
    "style_score": 0.25,
    "combined_score": 0.599,
    "label": "We can't tell whether this was written by a p…",
    "error": null,
    "elapsed_s": 0.206,
    "logged_as": [
      "decided"
    ],
    "sent": "It was the best of times, it was the worst of times, it was "
  },
  {
    "status": 200,
    "guess": "human",
    "model_score": 0.461,
    "style_score": 0.2055,
    "combined_score": 0.3332,
    "label": "We think this was written by a person.…",
    "error": null,
    "elapsed_s": 0.175,
    "logged_as": [
      "decided"
    ],
    "sent": "You don't know about me without you have read a book by the "
  }
]
```

Criterion 4 — one real appeal (log for that id: decision, then appeal) and one
appeal to an id that doesn't exist:

```json
[
  {
    "kind": "real",
    "submit_status": 200,
    "content_id": "4dce9293-7350-4c97-81fd-929e5b8ecc5a",
    "appeal_status": 200,
    "log_statuses": [
      "decided",
      "under_review"
    ]
  },
  {
    "kind": "bogus",
    "content_id": "does-not-exist-t1",
    "appeal_status": 404,
    "log_statuses": []
  }
]
```

Criterion 5 — all four malformed requests:

```json
[
  {
    "status": 400,
    "guess": null,
    "model_score": null,
    "style_score": null,
    "combined_score": null,
    "label": null,
    "error": "missing_text",
    "elapsed_s": 0.009,
    "logged_as": [
      "rejected"
    ],
    "sent": "(empty text)"
  },
  {
    "status": 400,
    "guess": null,
    "model_score": null,
    "style_score": null,
    "combined_score": null,
    "label": null,
    "error": "missing_text",
    "elapsed_s": 0.01,
    "logged_as": [
      "rejected"
    ],
    "sent": "{\"creator_id\": \"eval_bad_missing\"}"
  },
  {
    "status": 400,
    "guess": null,
    "model_score": null,
    "style_score": null,
    "combined_score": null,
    "label": null,
    "error": "missing_text",
    "elapsed_s": 0.01,
    "logged_as": [
      "rejected"
    ],
    "sent": "{\"text\": null, \"creator_id\": \"eval_bad_null\"}"
  },
  {
    "status": 413,
    "guess": null,
    "model_score": null,
    "style_score": null,
    "combined_score": null,
    "label": null,
    "error": "text_too_long",
    "elapsed_s": 0.013,
    "logged_as": [
      "rejected"
    ],
    "sent": "word word word word word word word word word word word word "
  }
]
```

**Diagnoses**

Stages: the route (`app.py::submit`), signal one (`detector.model_signal`,
gpt2 perplexity), signal two (`stylometry.style_signal`: sentence-length
spread 60%, punctuation density 30%, type-token ratio 10%), the combining rule
(`scoring.combine_signals`: equal-weight average, capped at 0.64 unless both
signals are ≥ 0.6), and the label mapping (`config.py` thresholds 0.35 / 0.65).

*Pattern A — the two signals both reward plainness, so on plain human writing
they agree, and the agreement floor can't help.* (FP02, FP03, FP04, FP05,
criterion 1 #10.) The floor was built for the case where the signals
disagree. On formal, technical, rubric or second-language writing they fail
together: plain words are predictable to gpt2 (signal one 0.74–0.83), and the
same texts have almost no expressive punctuation (FP03: 0.000 per word, FP02:
0.013, FP05: 0.029) and even sentence lengths (spread 0.24–0.33), so signal
two reads them as AI too (0.68–0.85). Both clear 0.6, the cap doesn't fire,
the average lands at 0.75–0.83, and the label mapping at 0.65 turns that into
an accusation. Criterion 1's miss is the same mechanism on a gentler text:
Jane Eyre's paragraph is three long sentences of similar length (spread
0.278) with few marks (0.091), so 0.688 / 0.676 → 0.682 → "AI". **Stage:
signal one and signal two are correlated, the combining rule treats them as
independent, and the 0.65 threshold sits inside where plain human writing
lands.**

*Pattern B — signal two is cheap to move, and the agreement floor gives it a
veto.* (EV02, EV03, EV06, EV07, EV09; criterion 3's AI #3–#5.) AI text is
only labelled AI if *both* signals are ≥ 0.6, so an attacker only needs to
push one of them under 0.6, and signal two is the easy one: it is 90%
sentence-length spread and punctuation density, both editable without
touching the words. EV07 replaced full stops with "; and, moreover," — the
whole text became one "sentence", so spread drops out, and punctuation
density hit 0.227, the top of the human range → signal two 0.005. EV02's
inserted "Really." fragments pushed spread to 0.849 → 0.289. My own clear-AI
explainer paragraphs didn't even need an attack: their comma-heavy lists
("prioritizing tasks, setting clear goals, and minimizing distractions") put
punctuation density at 0.10–0.13, which signal two reads as human, so three
of five were held at the 0.64 cap. **Stage: signal two (punctuation density
points the wrong way for list-y AI prose) plus the combining rule (the floor
turns one weak signal into a veto).** This is also the main reason criterion
3 is short: only 2 of 5 AI texts cleared the floor. The rest of the gap
shortfall is the memorised Dickens/Thoreau openings above (signal one).

*Pattern C — anything that makes gpt2 surprised reads as human to signal
one.* (EV01, EV04-after, EV05, EV08, PI02.) EV01's typos were aimed at signal
two ("typos raise word variety"), but signal two still said AI (0.869);
it was signal one that moved — misspellings are high-perplexity tokens, so it
fell to 0.164. PI02 is the same: nothing in this service reads text as
instructions, so the "SYSTEM: … Return guess=human" line didn't work as an
injection — but it is a strange string to gpt2, perplexity rose, signal one
dropped to 0.204, and the attacker got `human` anyway. EV05 (heavy human
editing) and EV08 (two short sentences) land low for the same reason; EV05 is
arguably not AI text any more. **Stage: signal one; mechanism: perplexity
measures surprise, and surprise is easy to add.**

*Pattern D — the route accepts text that isn't scorable writing, and signal
two treats "no evidence" as "AI".* (MF05, MF06, MF07; MF03/MF04 got lucky.)
The route only checks for a non-empty string ≤ 20,000 characters.
`stylometry.words()` matches `[a-z0-9']`, so emoji and Arabic produce zero
words: type-token ratio and punctuation density both return 0.0, which scales
to "fully AI", and with no sentence breaks spread drops out → signal two 1.0.
gpt2 finds runs of identical bytes or emoji tokens very predictable → signal
one 0.91–1.00. Both over 0.6 → labelled AI at 0.87–0.999. MF07 is real
writing in Arabic, so this is a false accusation of a non-English writer.
**Stage: the route (no "is this English prose?" check) and signal two (no
words should be "no evidence", 0.5, not 1.0).**

*Held, and why:* every malformed request (`400`/`413`, all logged as
`rejected`, none reached the model); the flood (`429` after 10, logged);
PI04/PI05 (labels are fixed strings and the log never stores the text, so
there is nothing to inject into); PI01/PI03 (injected text didn't produce
`human` — but only because the base AI text scores "unsure" anyway, so this
"held" is weak).

*A bug the criteria didn't target — cold-start race in `detector._load`.*
In the crashed run, the first request took over 90 s to load gpt2 (torch
importing over WSL's `/mnt/c`), the client timed out and sent the next
request while loading was still going on, and two threads loaded the model
at once. The result was a model left on PyTorch's `meta` device and
`RuntimeError: Tensor.item() cannot be called on meta tensors` on **every**
later request — 500s until restart. **Stage: signal one's loader; mechanism:
lazy loading with no lock under Flask's threaded server.** Criterion 5 would
not catch it, because the refusals happen before the model is touched.

---

## The Improvement

**What I changed:** one line in `config.py` — `AI_THRESHOLD` from **0.65 to
0.80**. The unsure band is now 0.35–0.80 instead of 0.35–0.65. Because the
combining rule's cap is `AI_THRESHOLD - 0.01`, split-signal texts now cap at
0.79 instead of 0.64; that follows from the same line and is not a separate
change. Nothing else moved: same weights, floor, signals, route and labels.
(Committed in `d2f22ec`.)

**Which diagnosis pointed at it:** Pattern A. The expensive mistake is a
wrong accusation (criteria.md), and every accusation of human text sat
between 0.68 and 0.83 with both signals agreeing — a region the agreement
floor can't reach. The root cause is the correlated signals, but fixing that
means redesigning signal two; the threshold is the one lever that moves those
scores out of the accusing band without touching a signal. 0.80 is the
smallest round number above FP02/FP03/FP04 and the Jane Eyre paragraph. I
chose it *after* seeing those scores, which risks fitting the threshold to
this particular attack set — the honest test would be a fresh set of human
writing.

`python run_attacks.py --set attack_set --label after` →
[results/attack_run_2026-11-11_0243_after.md](results/attack_run_2026-11-11_0243_after.md),
and `python run_eval.py --label after` →
[results/run_2026-11-11_0243_after.md](results/run_2026-11-11_0243_after.md).

### Attack Run — After

Same inputs, same marking rules. ⟵ marks a verdict that changed.

| ID | Family | Before: guess (combined) | After: guess (combined) | Before | After |
|---|---|---|---|---|---|
| EV01 | evasion | unsure (0.516) | unsure (0.516) | BROKE | **BROKE** |
| EV02 | evasion | unsure (0.442) | unsure (0.442) | BROKE | **BROKE** |
| EV03 | evasion | unsure (0.575) | unsure (0.575) | BROKE | **BROKE** |
| EV04 | evasion | ai (0.718) | unsure (0.718) | HELD | **BROKE** ⟵ |
| EV05 | evasion | human (0.262) | human (0.262) | BROKE | **BROKE** |
| EV06 | evasion | unsure (0.437) | unsure (0.437) | BROKE | **BROKE** |
| EV07 | evasion | human (0.295) | human (0.295) | BROKE | **BROKE** |
| EV08 | evasion | unsure (0.500) | unsure (0.500) | BROKE | **BROKE** |
| EV09 | evasion | unsure (0.610) | unsure (0.610) | BROKE | **BROKE** |
| EV10 | evasion | ai (0.857) | ai (0.857) | HELD | **HELD** |
| FP01 | false_positive | unsure (0.600) | unsure (0.600) | HELD | **HELD** |
| FP02 | false_positive | ai (0.786) | unsure (0.786) | BROKE | **HELD** ⟵ |
| FP03 | false_positive | ai (0.761) | unsure (0.761) | BROKE | **HELD** ⟵ |
| FP04 | false_positive | ai (0.754) | unsure (0.754) | BROKE | **HELD** ⟵ |
| FP05 | false_positive | ai (0.826) | ai (0.826) | BROKE | **BROKE** |
| FP06 | false_positive | unsure (0.640) | unsure (0.708) | HELD | **HELD** |
| FP07 | false_positive | unsure (0.640) | unsure (0.641) | HELD | **HELD** |
| FP08 | false_positive | unsure (0.457) | unsure (0.457) | HELD | **HELD** |
| PI01 | prompt_injection | unsure (0.402) | unsure (0.402) | HELD | **HELD** |
| PI02 | prompt_injection | human (0.273) | human (0.273) | BROKE | **BROKE** |
| PI03 | prompt_injection | unsure (0.622) | unsure (0.622) | HELD | **HELD** |
| PI04 | prompt_injection | unsure (0.460) | unsure (0.460) | HELD | **HELD** |
| PI05 | prompt_injection | unsure (0.445) | unsure (0.445) | HELD | **HELD** |
| PI06 | prompt_injection | unsure (0.576) | unsure (0.576) | HELD | **HELD** |
| MF01 | malformed | 400 | 400 | HELD | **HELD** |
| MF02 | malformed | 400 | 400 | HELD | **HELD** |
| MF03 | malformed | unsure (0.375) | unsure (0.375) | HELD | **HELD** |
| MF04 | malformed | unsure (0.506) | unsure (0.506) | HELD | **HELD** |
| MF05 | malformed | ai (0.874) | ai (0.874) | BROKE | **BROKE** |
| MF06 | malformed | ai (0.999) | ai (0.999) | BROKE | **BROKE** |
| MF07 | malformed | ai (0.953) | ai (0.953) | BROKE | **BROKE** |
| MF08 | malformed | 413 | 413 | HELD | **HELD** |
| RQ01 | malformed | 400 | 400 | HELD | **HELD** |
| RQ02 | malformed | unsure (0.495) | unsure (0.495) | HELD | **HELD** |
| RQ03 | malformed | 400 | 400 | HELD | **HELD** |
| RQ04 | malformed | 400 | 400 | HELD | **HELD** |
| RQ05 | malformed | 400 | 400 | HELD | **HELD** |
| RQ06 | malformed | unsure (0.400) | unsure (0.400) | HELD | **HELD** |
| RQ07 | malformed | 400 | 400 | HELD | **HELD** |
| RQ08 | malformed | 400 | 400 | HELD | **HELD** |
| RQ09 | malformed | 400 | 400 | HELD | **HELD** |
| RQ10 | malformed | 400 | 400 | HELD | **HELD** |
| RQ11 | malformed | 400 | 400 | HELD | **HELD** |
| RQ12 | malformed | 400 | 400 | HELD | **HELD** |
| FL01_01 | flood_same_creator | unsure (0.389) | unsure (0.389) | HELD | **HELD** |
| FL01_02 | flood_same_creator | unsure (0.389) | unsure (0.389) | HELD | **HELD** |
| FL01_03 | flood_same_creator | unsure (0.389) | unsure (0.389) | HELD | **HELD** |
| FL01_04 | flood_same_creator | unsure (0.389) | unsure (0.389) | HELD | **HELD** |
| FL01_05 | flood_same_creator | unsure (0.389) | unsure (0.389) | HELD | **HELD** |
| FL01_06 | flood_same_creator | unsure (0.389) | unsure (0.389) | HELD | **HELD** |
| FL01_07 | flood_same_creator | unsure (0.389) | unsure (0.389) | HELD | **HELD** |
| FL01_08 | flood_same_creator | unsure (0.389) | unsure (0.389) | HELD | **HELD** |
| FL01_09 | flood_same_creator | unsure (0.389) | unsure (0.389) | HELD | **HELD** |
| FL01_10 | flood_same_creator | unsure (0.389) | unsure (0.389) | HELD | **HELD** |
| FL01_11 | flood_same_creator | 429 | 429 | HELD | **HELD** |
| FL01_12 | flood_same_creator | 429 | 429 | HELD | **HELD** |

| Family | Held | Broke |
|---|---|---|
| evasion | 1 | 9 |
| false_positive | 7 | 1 |
| prompt_injection | 5 | 1 |
| malformed | 17 | 3 |
| flood_same_creator | 12 | 0 |
| **total** | **42** | **14** |

| | Before | After |
|---|---|---|
| Human texts accused (false_positive family) | 4 of 8 | **1 of 8** (FP05) |
| AI texts flagged (evasion family) | 2 of 10 | **1 of 10** (EV10) |
| Malformed text labelled AI | 3 | 3 |
| Total held / broke | 40 / 16 | **42 / 14** |

### Run Log — After

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. My own writing is never called AI | 0 AI and ≤ 3 unsure | 0 AI, 7 unsure | 0 AI, 7 unsure | 0 AI, 7 unsure | **MISSED** (was 1 AI, 6 unsure) |
| 2. Plain writing isn't treated as machine writing | ≤ 1 of 5 AI | 1/5 | 1/5 | 1/5 | **MET** (unchanged) |
| 3. Clearly AI and clearly human score far apart | gap ≥ 0.30 and ≥ 3/5 caught | gap 0.230, 1/5 | gap 0.230, 1/5 | gap 0.230, 1/5 | **MISSED** (was 0.212, 2/5) |
| 4. Every appeal recorded | 5/5 + 3/3 | 5/5, 3/3 | 5/5, 3/3 | 5/5, 3/3 | **MET** |
| 5. Bad input gets a clear refusal | 4/4 | 4/4 | 4/4 | 4/4 | **MET** |

**Did it help, and how do I know:** It helped with what it was aimed at, and
it cost about what it should. Wrong accusations of human writing in the
attack set fell from 4 of 8 to 1 of 8 (FP02, FP03, FP04 are now "unsure" at
the same scores — the scores didn't change, the line did), and criterion 1's
one accusation is gone. But criterion 1 is still **MISSED**: the Jane Eyre
paragraph moved into "unsure", so unsure went from 6 to 7, and the target
allows 3. The cost landed on the other side, as the threshold comment in
`config.py` predicted: clear-AI texts caught fell from 2 of 5 to 1 of 5, and
EV04 (0.718) now gets through, so evasion is 9 of 10. Criterion 3's gap only
"improved" (0.212 → 0.230) because the cap moved from 0.64 to 0.79 and stopped
flattening the AI scores. That's not real separation, and criterion 3 is a
worse miss than before. One sentence: **the change traded one AI catch for
three fewer accusations, which is the trade criteria.md says to make, but it
didn't bring any missed criterion to MET.**

---

## What's Still Broken

- **FP05 — technical documentation still accused (0.826).** Both signals are
  over 0.8; no threshold below 0.83 would save it. *What I'd do:* fix Pattern
  A at its source by dropping punctuation density from signal two, or
  replacing it with something plain writing doesn't fail, then recalibrating.
  *Why I stopped:* one change per unit, and that's a signal redesign that
  would also move every other score.
- **MF05/MF06/MF07 — non-text and non-English labelled AI.** *What I'd do:*
  in the route, refuse text with too few Latin-alphabet words, with a 422
  that says "we can only check English prose" rather than a label; and in
  `style_signal`, return 0.5 (no evidence) when there are no words. *Why I
  stopped:* one change; I picked the false-positive fix because accused human
  writers are far more common than emoji submissions. MF07 is the one I'd fix
  next — it's a real person writing in their own language.
- **Evasions (9 of 10) and PI02.** *What I'd do:* nothing quick. Signal two's
  measures can be edited without touching the words, and signal one is
  fooled by anything surprising. Catching these means stronger signals, and
  any threshold change that catches them brings back the accusations above.
  *Why I stopped:* this is the side of the trade I chose to lose.
- **Criterion 1 — 7 of 10 human texts "unsure".** Ordinary published prose
  scores 0.44–0.55 on signal one, because gpt2's 45-perplexity midpoint sits
  right where normal narrative prose lands. *What I'd do:* recalibrate
  `model_signal`'s midpoint on a held-out set of human writing, and re-run
  criterion 1 with ten pieces I actually wrote. *Why I stopped:* one change,
  and the stand-in text makes this criterion's number less trustworthy than
  the others.
- **Criterion 3 — 1 of 5 AI caught, gap 0.23.** Pattern B (signal two's veto)
  plus memorised human openings in the test set. *What I'd do:* replace
  Dickens/Thoreau with mid-book passages — that's a fix to the measurement,
  not the system — then address signal two as above.
- **Cold-start race in `detector._load`.** Two requests during the first model
  load leave the model unusable, and every later request gets a 500. *What I'd
  do:* load the model at startup, or put a `threading.Lock` around `_load`.
  *Why I stopped:* the one-change rule, and it only bites on a cold start.
  It's the first thing I'd fix before this ran anywhere real, because it
  fails silently for everyone.

**The trade I'd make if this ran for real:** I'd keep the wider band and
accept more AI text getting through as "unsure". The people who pay are
honest writers competing with people who used AI, and readers who trust a
"person" label more than they should. The other way round, the cost lands on
individual writers — disproportionately second-language and plain-style
writers, as FP03 showed — who get accused in public and have to prove a
negative to clear their name.

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
       [x] At least four new commits
       [ ] Repository URL submitted — WRITE IT DOWN

     SUBMISSION CHECKLIST — unit 8

       [x] Rate limiting on /submit, with your numbers justified
       [x] The pasted run of status codes showing 429
       [x] Audit log with all nine fields, recording rejections too
       [x] The attack set run IN FULL, every input with an outcome
       [x] Ten audit log entries pasted as text
       [x] Five criteria across three trials
       [x] A diagnosis for every miss and every broken attack — stage AND mechanism
       [x] One improvement, with Attack Run — After
       [x] What's Still Broken, including the production trade
       [x] At least four new commits
       [ ] The SAME repository URL as last unit

     Do not delete and recreate this repository.
     ═════════════════════════════════════════════════════════════════════ -->

---

📖 **How to run this project: [RUNNING.md](RUNNING.md)**
