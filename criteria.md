# Acceptance criteria — Provenance Guard

Five criteria that say what "working" means for this service, written in unit 7
**before** you built it.

**All five are yours.** None are given.

An acceptance criterion names a number or something plainly observable. *"The
detector is accurate"* is an opinion — and perfect AI detection isn't possible
anyway, so it's an opinion about something nobody can deliver. *"Of 10 pieces I
wrote myself, at most 1 is labelled high-confidence AI"* is a criterion.

Under each, write a sentence or two on **why that target**. *"I allow at most 1
false positive in 10 because on a writing site a wrong accusation costs more
than a missed detection"* is a real answer.

> Missing your own targets next unit costs you nothing. Setting a target so
> easy you can't miss it does.

---

## Pick numbers you can defend

**Cover at least three of these five areas.** They're prompts, not a form.

| Area | A question it could answer |
|---|---|
| False positives | How often may a human's writing get called AI? |
| Score spread | How far apart should clearly-AI and clearly-human text score? |
| Label coverage | Is every one of your three labels actually reachable? |
| The appeal path | Does an appeal always change status and always get recorded? |
| Bad input | What happens when `text` is missing, empty, or enormous? |

Two things worth knowing before you pick numbers:

- **The expensive mistake is one-sided.** Missing some AI text costs the site a
  little. Accusing a real writer costs that person a lot. A criterion that
  treats both errors as equally bad is describing a system nobody would ship.
- **Unit 8 tests across three trials, and the target has to hold across all
  three.** Your first signal runs a model, so identical input can score
  differently twice. A target of "at most 1 in 10" against trials of 2, 1, 2 is
  a **miss**.

---
## 1. My own writing is never called AI

Of 10 pieces I wrote myself, **0** are labelled high-confidence AI and **at
most 3** are labelled unsure — in every one of three trials.

**Why this target:**

A wrong accusation is the expensive mistake. It lands on a real person,
and on a writing site that person may have no easy way to prove their
innocence. "Unsure" doesn't accuse anyone, so I can tolerate some, but if most
of my own work comes back unsure the label stops meaning anything. Zero
high-confidence AI labels is strict on purpose: with only 10 pieces, even one
wrong accusation is a 10% false-positive rate.

---

## 2. Plain writing isn't treated as machine writing

Of 5 human paragraphs written plainly on purpose (short sentences, common
words, the way a second-language writer might write), **at most 1** is
labelled high-confidence AI — in every one of three trials.

**Why this target:**

This is the writer both signals are most likely to accuse (see the blind spots
in the README), and the one with the least room to argue back. Criterion 1
uses my normal writing, which may hide the problem. This one tests it head on.
I allow 1 rather than 0 because I expect gpt2 to score this kind of text very
predictable, and a target I'm certain to miss teaches me nothing. If it hits
2 or more, the combining rule is letting one signal convict on its own.

---

## 3. Clearly AI and clearly human text score far apart

On 5 clearly AI-generated texts and 5 clearly human ones, the AI group's
average combined score is **at least 0.30 higher** than the human group's, and
**at least 3 of the 5** AI texts are labelled high-confidence AI — in every
one of three trials.

**Why this target:**

If the easy cases don't separate, nothing harder will. A 0.30 gap is the
width of the unsure band (0.35–0.65), so a smaller gap means even
obvious cases tend to land in the middle. The 3-of-5 catch rate keeps
criteria 1 and 2 honest: a service that labels everything "unsure" would pass
both of those and be useless. I aim for 3 of 5, not 5 of 5, because I've
chosen to lose some AI text rather than accuse people.

---

## 4. Every appeal is recorded, and a bad one changes nothing

Of 5 appeals sent against real `content_id`s, **5 of 5** return `200` and
add a log entry with status `under_review` while leaving the original
decision in the log. Of 3 appeals sent with a `content_id` that doesn't exist,
**3 of 3** return `404` and add no `under_review` entry.

**Why this target:**

The appeal is the only thing between a wrong accusation and nothing at all, so
"usually works" isn't good enough. Anything less than every time means some
writer's challenge silently disappeared. The bad-id half matters because a
typo that "succeeds" tells the writer their appeal is in when it isn't.

---

## 5. Bad input gets a clear refusal, never a crash

Of 4 malformed requests (empty `text`, no `text` field, `text` set to `null`,
and `text` of 50,000 words), **4 of 4** get a `400` or `413` with a JSON error
message, **0** get a `500`, each answers in **under 5 seconds**, and each
writes a `rejected` entry to the audit log.

**Why this target:**

Malformed input is one of the most common ways real services fail, and unit
8's attack set will send it whether I plan for it or not. A `500` tells the
caller nothing and can mean the service crashed. The 5-second limit catches
the 50,000-word case being fed to the model instead of refused. The log entry
matters because a rejected request that leaves no trace is invisible when I
diagnose attacks later.

---

<!-- ─────────────────────────────────────────────────────────────────────────
     UNIT 8 — read this before you change anything above.

     If a criterion turns out to be BROKEN rather than merely unmet, you can
     revise it, and that earns credit. But never delete or edit the original
     line. Add the revision underneath, like this:

         ## 2. Uncertain cases land in the unsure band

         The system handles uncertain cases well.

         **Why this target:** ...

         > **Revised in unit 8:** Text I judged borderline scores between
         > 0.4 and 0.6 in at least 4 of 5 cases.
         >
         > **Why revised:** "well" gave me nothing to check. I couldn't
         > reach a verdict from it at all.

     That's a revision because the criterion couldn't be MEASURED.

     Lowering a target because you missed it is not a revision, and it costs
     you the point:

         ✗ "At most 1 of 10 of my own pieces flagged as AI" → "at most 3
            of 10", because 1 of 10 turned out to be hard.

     A number you missed stays where it is, gets diagnosed, and gets a fix
     attempted. That's where the points are.
     ───────────────────────────────────────────────────────────────────────── -->
