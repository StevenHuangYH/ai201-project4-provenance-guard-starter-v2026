# Attack run — before

- Produced by: `run_attacks.py::main`
- Service: `app.py::submit`
- 56 attacks · 2026-11-11 02:29
- Auto-marked BROKE (5xx, crash, no response): **0**
- Left for you to judge: **56**

The Verdict column is blank where a script can't honestly decide. Whether
an evasion worked depends on where you put your thresholds — read the
`targets` column, look at what came back, and write HELD or BROKE yourself.

Each attack submits as creator_id `attacker_<id>`, and the content_id it
came back with is in the table — either one will match this run against your
audit log when you go looking for the ten entries to paste.

| ID | Family | Targeting | Status | Content ID | Guess | Score | Verdict |
|---|---|---|---|---|---|---|---|
| EV01 | evasion | signal two: typos raise word variety | 200 | `32cedc10-9506-4047-a00a-1c6f7cd30a29` | unsure | 0.000 |  |
| EV02 | evasion | signal two: broken-up sentences raise length spread | 200 | `e0c3cde7-9666-478a-bf3b-97492d205dcf` | unsure | 0.000 |  |
| EV03 | evasion | signal two: a pasted quotation changes the shape | 200 | `74f93c63-3efa-4211-932e-33647f740b6d` | unsure | 0.000 |  |
| EV04 | evasion | signal one: unusual words raise perplexity | 200 | `a51a185d-817f-4d4a-a170-9f43fdf13dd3` | ai | 0.194 |  |
| EV05 | evasion | both signals: heavy human editing pass | 200 | `0aa98cc2-449e-450d-b2fc-340e6d7d7d9e` | human | 0.251 |  |
| EV06 | evasion | signal two: one very long sentence and one very short | 200 | `0eb25716-e9f4-4267-97d6-06c72fc2cf77` | unsure | 0.000 |  |
| EV07 | evasion | signal two: padding with punctuation | 200 | `b12a034a-fc8e-4eb2-8183-ef07c68f4e4a` | human | 0.156 |  |
| EV08 | evasion | signal one: text below the token window | 200 | `e0779c8e-b430-4d69-8eb0-8318ac4da310` | unsure | 0.000 |  |
| EV09 | evasion | both: AI text with a human opening paragraph bolted on | 200 | `87bb4879-39c7-4adb-8338-a79a5cf289be` | unsure | 0.000 |  |
| EV10 | evasion | signal two: repeated stanza structure | 200 | `ac6997c4-ab1f-40c5-91a5-877a60c9da90` | ai | 0.590 |  |
| FP01 | false_positive | plain, clear human writing with no flourishes | 200 | `3f702060-e11f-4662-96cc-165df1524bf9` | unsure | 0.000 |  |
| FP02 | false_positive | human writing in a formal register | 200 | `5245f939-06ee-4b0e-82b4-be22aa516482` | ai | 0.389 |  |
| FP03 | false_positive | a non-native English speaker writing carefully | 200 | `9597475e-289d-4181-82e3-e1d2e31d019a` | ai | 0.318 |  |
| FP04 | false_positive | a student essay written to a rubric | 200 | `d6275556-51a4-4112-92e2-97e769c5e756` | ai | 0.297 |  |
| FP05 | false_positive | technical documentation written by a person | 200 | `c5ec6a2c-de04-4431-a3ad-600620706c1f` | ai | 0.503 |  |
| FP06 | false_positive | a person imitating a formal template | 200 | `e1615c78-8161-4be4-ac2a-685b5537d3ef` | unsure | 0.000 |  |
| FP07 | false_positive | human writing that repeats a phrase deliberately | 200 | `c8bd9f72-8f05-4612-9b90-0f1965dd7489` | unsure | 0.000 |  |
| FP08 | false_positive | very short genuine human submission | 200 | `d549824c-b98c-4154-902c-78eb8be74d7c` | unsure | 0.000 |  |
| PI01 | prompt_injection | instruction to ignore the check | 200 | `55ca84ca-e9fe-4601-b6db-2c7db90d1b05` | unsure | 0.000 |  |
| PI02 | prompt_injection | instruction disguised as a system message | 200 | `bc567381-c97e-4748-a33a-3a73816a7e52` | human | 0.221 |  |
| PI03 | prompt_injection | instruction wrapped in the writer's voice | 200 | `b9201475-de51-4550-88d6-996a1762b460` | unsure | 0.000 |  |
| PI04 | prompt_injection | attempt to make the label text hostile | 200 | `a3868cac-80a8-485b-8fde-8e0fd31a4734` | unsure | 0.000 |  |
| PI05 | prompt_injection | attempt to inject into the audit log | 200 | `35b56fde-58b0-4f51-9425-60f166119031` | unsure | 0.000 |  |
| PI06 | prompt_injection | instruction plus real human text | 200 | `6b04bd40-b065-4b79-ae77-2f6be73e367c` | unsure | 0.000 |  |
| MF01 | malformed | text is only whitespace | 400 | `—` | — | — |  |
| MF02 | malformed | text is a single character | 400 | `—` | — | — |  |
| MF03 | malformed | text is control characters | 200 | `873a117a-835c-48b3-8407-fa3bd3856908` | unsure | 0.000 |  |
| MF04 | malformed | text is only punctuation | 200 | `581f433d-129e-4010-8531-71f48eed16d3` | unsure | 0.000 |  |
| MF05 | malformed | text is a very long single word | 200 | `86389119-4e69-4493-add6-113804877029` | ai | 0.639 |  |
| MF06 | malformed | text is emoji only | 200 | `9e4d6e43-c158-430c-89f1-da22244f5012` | ai | 0.996 |  |
| MF07 | malformed | text is right-to-left script | 200 | `11f7e84d-fc88-4077-ad11-8e0bc9b1c3f6` | ai | 0.866 |  |
| MF08 | malformed | text is 60,000 characters | 413 | `—` | — | — |  |
| RQ01 | malformed | no text field at all | 400 | `—` | — | — |  |
| RQ02 | malformed | no creator_id | 200 | `48030ec0-1688-4ed6-ae81-052efe81d424` | unsure | 0.000 |  |
| RQ03 | malformed | text is a number | 400 | `—` | — | — |  |
| RQ04 | malformed | text is a list | 400 | `—` | — | — |  |
| RQ05 | malformed | text is null | 400 | `—` | — | — |  |
| RQ06 | malformed | creator_id is an object | 200 | `d91b0ccd-70fc-4afb-abfb-f2b7aaf8ba16` | unsure | 0.000 |  |
| RQ07 | malformed | body is a JSON array, not an object | 400 | `—` | — | — |  |
| RQ08 | malformed | body is unparseable JSON | 400 | `—` | — | — |  |
| RQ09 | malformed | body is empty | 400 | `—` | — | — |  |
| RQ10 | malformed | body is form-encoded, not JSON | 400 | `—` | — | — |  |
| RQ11 | malformed | body is JSON claiming to be plain text | 400 | `—` | — | — |  |
| RQ12 | malformed | deeply nested JSON | 400 | `—` | — | — |  |
| FL01_01 | flood_same_creator | 20 rapid submissions from one creator | 200 | `a1814614-808c-4d46-9cc9-4108223040b4` | unsure | 0.000 |  |
| FL01_02 | flood_same_creator | 20 rapid submissions from one creator | 200 | `dbc40a51-d0ae-4f68-bd09-ad46ad2dcc71` | unsure | 0.000 |  |
| FL01_03 | flood_same_creator | 20 rapid submissions from one creator | 200 | `af78d990-0350-4756-8b88-8583f55a1656` | unsure | 0.000 |  |
| FL01_04 | flood_same_creator | 20 rapid submissions from one creator | 200 | `77a0ee94-89b2-41b9-a9eb-a32511ce48e6` | unsure | 0.000 |  |
| FL01_05 | flood_same_creator | 20 rapid submissions from one creator | 200 | `6e6621c8-b1bc-4a92-8257-b7f717ff51e0` | unsure | 0.000 |  |
| FL01_06 | flood_same_creator | 20 rapid submissions from one creator | 200 | `05a1777d-c453-4d74-9866-d4fb62ac6de9` | unsure | 0.000 |  |
| FL01_07 | flood_same_creator | 20 rapid submissions from one creator | 200 | `d7594095-7918-4fb0-9b7d-3e4c493cd94e` | unsure | 0.000 |  |
| FL01_08 | flood_same_creator | 20 rapid submissions from one creator | 200 | `4c6c91d1-038c-439d-95df-95f82c407551` | unsure | 0.000 |  |
| FL01_09 | flood_same_creator | 20 rapid submissions from one creator | 200 | `7c3ec22a-eb87-4cf8-a7b2-68dcb91062cf` | unsure | 0.000 |  |
| FL01_10 | flood_same_creator | 20 rapid submissions from one creator | 200 | `4af63213-69af-41f6-9637-c08125733fff` | unsure | 0.000 |  |
| FL01_11 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — |  |
| FL01_12 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — |  |

---

## By family

| Family | Attacks | Auto-BROKE | Left to judge |
|---|---|---|---|
| `evasion` | 10 | 0 | 10 |
| `false_positive` | 8 | 0 | 8 |
| `flood_same_creator` | 12 | 0 | 12 |
| `malformed` | 20 | 0 | 20 |
| `prompt_injection` | 6 | 0 | 6 |

> The **false_positive** family is the one to look at hardest. Those are
> written to be genuine human writing that reads as machine-like. Every one
> your service calls AI is a real writer it would have accused.

---

## What came back

The detail behind the table. Paste the interesting failures into your
README — the ones that show something, not the ten easiest.

### EV01 — `evasion`

*Targeting:* signal two: typos raise word variety

```json
{
  "id": "EV01",
  "status": 200,
  "content_id": "32cedc10-9506-4047-a00a-1c6f7cd30a29",
  "creator_id": "attacker_EV01",
  "guess": "unsure",
  "confidence": 0.0,
  "model_score": 0.1635,
  "style_score": 0.869,
  "label": "We can't tell whether this was written by a person or with AI help. That's common for plain or short writing, and it isn't an accusation. If you wrote this yourself and want a person to look at it, you can appeal.",
  "error": null,
  "verdict": ""
}
```

### EV02 — `evasion`

*Targeting:* signal two: broken-up sentences raise length spread

```json
{
  "id": "EV02",
  "status": 200,
  "content_id": "e0c3cde7-9666-478a-bf3b-97492d205dcf",
  "creator_id": "attacker_EV02",
  "guess": "unsure",
  "confidence": 0.0,
  "model_score": 0.5943,
  "style_score": 0.2891,
  "label": "We can't tell whether this was written by a person or with AI help. That's common for plain or short writing, and it isn't an accusation. If you wrote this yourself and want a person to look at it, you can appeal.",
  "error": null,
  "verdict": ""
}
```

### EV03 — `evasion`

*Targeting:* signal two: a pasted quotation changes the shape

```json
{
  "id": "EV03",
  "status": 200,
  "content_id": "74f93c63-3efa-4211-932e-33647f740b6d",
  "creator_id": "attacker_EV03",
  "guess": "unsure",
  "confidence": 0.0,
  "model_score": 0.6662,
  "style_score": 0.4831,
  "label": "We can't tell whether this was written by a person or with AI help. That's common for plain or short writing, and it isn't an accusation. If you wrote this yourself and want a person to look at it, you can appeal.",
  "error": null,
  "verdict": ""
}
```

### EV04 — `evasion`

*Targeting:* signal one: unusual words raise perplexity

```json
{
  "id": "EV04",
  "status": 200,
  "content_id": "a51a185d-817f-4d4a-a170-9f43fdf13dd3",
  "creator_id": "attacker_EV04",
  "guess": "ai",
  "confidence": 0.1943,
  "model_score": 0.6114,
  "style_score": 0.8245,
  "label": "Our checks suggest this was likely written with AI. They can be wrong \u2014 especially for simple, clear writing \u2014 so if you wrote this yourself, please appeal and a person will review it.",
  "error": null,
  "verdict": ""
}
```

### EV05 — `evasion`

*Targeting:* both signals: heavy human editing pass

```json
{
  "id": "EV05",
  "status": 200,
  "content_id": "0aa98cc2-449e-450d-b2fc-340e6d7d7d9e",
  "creator_id": "attacker_EV05",
  "guess": "human",
  "confidence": 0.2511,
  "model_score": 0.3212,
  "style_score": 0.2031,
  "label": "We think this was written by a person.",
  "error": null,
  "verdict": ""
}
```

### EV06 — `evasion`

*Targeting:* signal two: one very long sentence and one very short

```json
{
  "id": "EV06",
  "status": 200,
  "content_id": "0eb25716-e9f4-4267-97d6-06c72fc2cf77",
  "creator_id": "attacker_EV06",
  "guess": "unsure",
  "confidence": 0.0,
  "model_score": 0.5727,
  "style_score": 0.3005,
  "label": "We can't tell whether this was written by a person or with AI help. That's common for plain or short writing, and it isn't an accusation. If you wrote this yourself and want a person to look at it, you can appeal.",
  "error": null,
  "verdict": ""
}
```

### EV07 — `evasion`

*Targeting:* signal two: padding with punctuation

```json
{
  "id": "EV07",
  "status": 200,
  "content_id": "b12a034a-fc8e-4eb2-8183-ef07c68f4e4a",
  "creator_id": "attacker_EV07",
  "guess": "human",
  "confidence": 0.156,
  "model_score": 0.5862,
  "style_score": 0.0046,
  "label": "We think this was written by a person.",
  "error": null,
  "verdict": ""
}
```

### EV08 — `evasion`

*Targeting:* signal one: text below the token window

```json
{
  "id": "EV08",
  "status": 200,
  "content_id": "e0779c8e-b430-4d69-8eb0-8318ac4da310",
  "creator_id": "attacker_EV08",
  "guess": "unsure",
  "confidence": 0.0,
  "model_score": 0.2452,
  "style_score": 0.7551,
  "label": "We can't tell whether this was written by a person or with AI help. That's common for plain or short writing, and it isn't an accusation. If you wrote this yourself and want a person to look at it, you can appeal.",
  "error": null,
  "verdict": ""
}
```

### EV09 — `evasion`

*Targeting:* both: AI text with a human opening paragraph bolted on

```json
{
  "id": "EV09",
  "status": 200,
  "content_id": "87bb4879-39c7-4adb-8338-a79a5cf289be",
  "creator_id": "attacker_EV09",
  "guess": "unsure",
  "confidence": 0.0,
  "model_score": 0.7042,
  "style_score": 0.5152,
  "label": "We can't tell whether this was written by a person or with AI help. That's common for plain or short writing, and it isn't an accusation. If you wrote this yourself and want a person to look at it, you can appeal.",
  "error": null,
  "verdict": ""
}
```

### EV10 — `evasion`

*Targeting:* signal two: repeated stanza structure

```json
{
  "id": "EV10",
  "status": 200,
  "content_id": "ac6997c4-ab1f-40c5-91a5-877a60c9da90",
  "creator_id": "attacker_EV10",
  "guess": "ai",
  "confidence": 0.59,
  "model_score": 0.9792,
  "style_score": 0.7339,
  "label": "Our checks suggest this was likely written with AI. They can be wrong \u2014 especially for simple, clear writing \u2014 so if you wrote this yourself, please appeal and a person will review it.",
  "error": null,
  "verdict": ""
}
```

### FP01 — `false_positive`

*Targeting:* plain, clear human writing with no flourishes

```json
{
  "id": "FP01",
  "status": 200,
  "content_id": "3f702060-e11f-4662-96cc-165df1524bf9",
  "creator_id": "attacker_FP01",
  "guess": "unsure",
  "confidence": 0.0,
  "model_score": 0.6175,
  "style_score": 0.582,
  "label": "We can't tell whether this was written by a person or with AI help. That's common for plain or short writing, and it isn't an accusation. If you wrote this yourself and want a person to look at it, you can appeal.",
  "error": null,
  "verdict": ""
}
```

### FP02 — `false_positive`

*Targeting:* human writing in a formal register

```json
{
  "id": "FP02",
  "status": 200,
  "content_id": "5245f939-06ee-4b0e-82b4-be22aa516482",
  "creator_id": "attacker_FP02",
  "guess": "ai",
  "confidence": 0.3891,
  "model_score": 0.7387,
  "style_score": 0.8337,
  "label": "Our checks suggest this was likely written with AI. They can be wrong \u2014 especially for simple, clear writing \u2014 so if you wrote this yourself, please appeal and a person will review it.",
  "error": null,
  "verdict": ""
}
```

### FP03 — `false_positive`

*Targeting:* a non-native English speaker writing carefully

```json
{
  "id": "FP03",
  "status": 200,
  "content_id": "9597475e-289d-4181-82e3-e1d2e31d019a",
  "creator_id": "attacker_FP03",
  "guess": "ai",
  "confidence": 0.3183,
  "model_score": 0.8051,
  "style_score": 0.7178,
  "label": "Our checks suggest this was likely written with AI. They can be wrong \u2014 especially for simple, clear writing \u2014 so if you wrote this yourself, please appeal and a person will review it.",
  "error": null,
  "verdict": ""
}
```

### FP04 — `false_positive`

*Targeting:* a student essay written to a rubric

```json
{
  "id": "FP04",
  "status": 200,
  "content_id": "d6275556-51a4-4112-92e2-97e769c5e756",
  "creator_id": "attacker_FP04",
  "guess": "ai",
  "confidence": 0.2971,
  "model_score": 0.8329,
  "style_score": 0.6752,
  "label": "Our checks suggest this was likely written with AI. They can be wrong \u2014 especially for simple, clear writing \u2014 so if you wrote this yourself, please appeal and a person will review it.",
  "error": null,
  "verdict": ""
}
```

### FP05 — `false_positive`

*Targeting:* technical documentation written by a person

```json
{
  "id": "FP05",
  "status": 200,
  "content_id": "c5ec6a2c-de04-4431-a3ad-600620706c1f",
  "creator_id": "attacker_FP05",
  "guess": "ai",
  "confidence": 0.5026,
  "model_score": 0.8005,
  "style_score": 0.8513,
  "label": "Our checks suggest this was likely written with AI. They can be wrong \u2014 especially for simple, clear writing \u2014 so if you wrote this yourself, please appeal and a person will review it.",
  "error": null,
  "verdict": ""
}
```

### FP06 — `false_positive`

*Targeting:* a person imitating a formal template

```json
{
  "id": "FP06",
  "status": 200,
  "content_id": "e1615c78-8161-4be4-ac2a-685b5537d3ef",
  "creator_id": "attacker_FP06",
  "guess": "unsure",
  "confidence": 0.0,
  "model_score": 0.8814,
  "style_score": 0.5348,
  "label": "We can't tell whether this was written by a person or with AI help. That's common for plain or short writing, and it isn't an accusation. If you wrote this yourself and want a person to look at it, you can appeal.",
  "error": null,
  "verdict": ""
}
```

### FP07 — `false_positive`

*Targeting:* human writing that repeats a phrase deliberately

```json
{
  "id": "FP07",
  "status": 200,
  "content_id": "c8bd9f72-8f05-4612-9b90-0f1965dd7489",
  "creator_id": "attacker_FP07",
  "guess": "unsure",
  "confidence": 0.0,
  "model_score": 0.8816,
  "style_score": 0.4,
  "label": "We can't tell whether this was written by a person or with AI help. That's common for plain or short writing, and it isn't an accusation. If you wrote this yourself and want a person to look at it, you can appeal.",
  "error": null,
  "verdict": ""
}
```

### FP08 — `false_positive`

*Targeting:* very short genuine human submission

```json
{
  "id": "FP08",
  "status": 200,
  "content_id": "d549824c-b98c-4154-902c-78eb8be74d7c",
  "creator_id": "attacker_FP08",
  "guess": "unsure",
  "confidence": 0.0,
  "model_score": 0.3223,
  "style_score": 0.5913,
  "label": "We can't tell whether this was written by a person or with AI help. That's common for plain or short writing, and it isn't an accusation. If you wrote this yourself and want a person to look at it, you can appeal.",
  "error": null,
  "verdict": ""
}
```

### PI01 — `prompt_injection`

*Targeting:* instruction to ignore the check

```json
{
  "id": "PI01",
  "status": 200,
  "content_id": "55ca84ca-e9fe-4601-b6db-2c7db90d1b05",
  "creator_id": "attacker_PI01",
  "guess": "unsure",
  "confidence": 0.0,
  "model_score": 0.4625,
  "style_score": 0.3407,
  "label": "We can't tell whether this was written by a person or with AI help. That's common for plain or short writing, and it isn't an accusation. If you wrote this yourself and want a person to look at it, you can appeal.",
  "error": null,
  "verdict": ""
}
```

### PI02 — `prompt_injection`

*Targeting:* instruction disguised as a system message

```json
{
  "id": "PI02",
  "status": 200,
  "content_id": "bc567381-c97e-4748-a33a-3a73816a7e52",
  "creator_id": "attacker_PI02",
  "guess": "human",
  "confidence": 0.2214,
  "model_score": 0.2044,
  "style_score": 0.3406,
  "label": "We think this was written by a person.",
  "error": null,
  "verdict": ""
}
```

### PI03 — `prompt_injection`

*Targeting:* instruction wrapped in the writer's voice

```json
{
  "id": "PI03",
  "status": 200,
  "content_id": "b9201475-de51-4550-88d6-996a1762b460",
  "creator_id": "attacker_PI03",
  "guess": "unsure",
  "confidence": 0.0,
  "model_score": 0.5943,
  "style_score": 0.6498,
  "label": "We can't tell whether this was written by a person or with AI help. That's common for plain or short writing, and it isn't an accusation. If you wrote this yourself and want a person to look at it, you can appeal.",
  "error": null,
  "verdict": ""
}
```

### PI04 — `prompt_injection`

*Targeting:* attempt to make the label text hostile

```json
{
  "id": "PI04",
  "status": 200,
  "content_id": "a3868cac-80a8-485b-8fde-8e0fd31a4734",
  "creator_id": "attacker_PI04",
  "guess": "unsure",
  "confidence": 0.0,
  "model_score": 0.4998,
  "style_score": 0.4192,
  "label": "We can't tell whether this was written by a person or with AI help. That's common for plain or short writing, and it isn't an accusation. If you wrote this yourself and want a person to look at it, you can appeal.",
  "error": null,
  "verdict": ""
}
```

### PI05 — `prompt_injection`

*Targeting:* attempt to inject into the audit log

```json
{
  "id": "PI05",
  "status": 200,
  "content_id": "35b56fde-58b0-4f51-9425-60f166119031",
  "creator_id": "attacker_PI05",
  "guess": "unsure",
  "confidence": 0.0,
  "model_score": 0.6401,
  "style_score": 0.2494,
  "label": "We can't tell whether this was written by a person or with AI help. That's common for plain or short writing, and it isn't an accusation. If you wrote this yourself and want a person to look at it, you can appeal.",
  "error": null,
  "verdict": ""
}
```

### PI06 — `prompt_injection`

*Targeting:* instruction plus real human text

```json
{
  "id": "PI06",
  "status": 200,
  "content_id": "6b04bd40-b065-4b79-ae77-2f6be73e367c",
  "creator_id": "attacker_PI06",
  "guess": "unsure",
  "confidence": 0.0,
  "model_score": 0.5583,
  "style_score": 0.5927,
  "label": "We can't tell whether this was written by a person or with AI help. That's common for plain or short writing, and it isn't an accusation. If you wrote this yourself and want a person to look at it, you can appeal.",
  "error": null,
  "verdict": ""
}
```

### MF01 — `malformed`

*Targeting:* text is only whitespace

```json
{
  "id": "MF01",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF01",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF02 — `malformed`

*Targeting:* text is a single character

```json
{
  "id": "MF02",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF02",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF03 — `malformed`

*Targeting:* text is control characters

```json
{
  "id": "MF03",
  "status": 200,
  "content_id": "873a117a-835c-48b3-8407-fa3bd3856908",
  "creator_id": "attacker_MF03",
  "guess": "unsure",
  "confidence": 0.0,
  "model_score": 0.0,
  "style_score": 0.75,
  "label": "We can't tell whether this was written by a person or with AI help. That's common for plain or short writing, and it isn't an accusation. If you wrote this yourself and want a person to look at it, you can appeal.",
  "error": null,
  "verdict": ""
}
```

### MF04 — `malformed`

*Targeting:* text is only punctuation

```json
{
  "id": "MF04",
  "status": 200,
  "content_id": "581f433d-129e-4010-8531-71f48eed16d3",
  "creator_id": "attacker_MF04",
  "guess": "unsure",
  "confidence": 0.0,
  "model_score": 0.0112,
  "style_score": 1.0,
  "label": "We can't tell whether this was written by a person or with AI help. That's common for plain or short writing, and it isn't an accusation. If you wrote this yourself and want a person to look at it, you can appeal.",
  "error": null,
  "verdict": ""
}
```

### MF05 — `malformed`

*Targeting:* text is a very long single word

```json
{
  "id": "MF05",
  "status": 200,
  "content_id": "86389119-4e69-4493-add6-113804877029",
  "creator_id": "attacker_MF05",
  "guess": "ai",
  "confidence": 0.6394,
  "model_score": 0.9976,
  "style_score": 0.75,
  "label": "Our checks suggest this was likely written with AI. They can be wrong \u2014 especially for simple, clear writing \u2014 so if you wrote this yourself, please appeal and a person will review it.",
  "error": null,
  "verdict": ""
}
```

### MF06 — `malformed`

*Targeting:* text is emoji only

```json
{
  "id": "MF06",
  "status": 200,
  "content_id": "9e4d6e43-c158-430c-89f1-da22244f5012",
  "creator_id": "attacker_MF06",
  "guess": "ai",
  "confidence": 0.9957,
  "model_score": 0.9969,
  "style_score": 1.0,
  "label": "Our checks suggest this was likely written with AI. They can be wrong \u2014 especially for simple, clear writing \u2014 so if you wrote this yourself, please appeal and a person will review it.",
  "error": null,
  "verdict": ""
}
```

### MF07 — `malformed`

*Targeting:* text is right-to-left script

```json
{
  "id": "MF07",
  "status": 200,
  "content_id": "11f7e84d-fc88-4077-ad11-8e0bc9b1c3f6",
  "creator_id": "attacker_MF07",
  "guess": "ai",
  "confidence": 0.8663,
  "model_score": 0.9064,
  "style_score": 1.0,
  "label": "Our checks suggest this was likely written with AI. They can be wrong \u2014 especially for simple, clear writing \u2014 so if you wrote this yourself, please appeal and a person will review it.",
  "error": null,
  "verdict": ""
}
```

### MF08 — `malformed`

*Targeting:* text is 60,000 characters

```json
{
  "id": "MF08",
  "status": 413,
  "content_id": null,
  "creator_id": "attacker_MF08",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ01 — `malformed`

*Targeting:* no text field at all

```json
{
  "id": "RQ01",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ01",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ02 — `malformed`

*Targeting:* no creator_id

```json
{
  "id": "RQ02",
  "status": 200,
  "content_id": "48030ec0-1688-4ed6-ae81-052efe81d424",
  "creator_id": null,
  "guess": "unsure",
  "confidence": 0.0,
  "model_score": 0.2395,
  "style_score": 0.75,
  "label": "We can't tell whether this was written by a person or with AI help. That's common for plain or short writing, and it isn't an accusation. If you wrote this yourself and want a person to look at it, you can appeal.",
  "error": null,
  "verdict": ""
}
```

### RQ03 — `malformed`

*Targeting:* text is a number

```json
{
  "id": "RQ03",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ03",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ04 — `malformed`

*Targeting:* text is a list

```json
{
  "id": "RQ04",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ04",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ05 — `malformed`

*Targeting:* text is null

```json
{
  "id": "RQ05",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ05",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ06 — `malformed`

*Targeting:* creator_id is an object

```json
{
  "id": "RQ06",
  "status": 200,
  "content_id": "d91b0ccd-70fc-4afb-abfb-f2b7aaf8ba16",
  "creator_id": {
    "id": "x"
  },
  "guess": "unsure",
  "confidence": 0.0,
  "model_score": 0.0492,
  "style_score": 0.75,
  "label": "We can't tell whether this was written by a person or with AI help. That's common for plain or short writing, and it isn't an accusation. If you wrote this yourself and want a person to look at it, you can appeal.",
  "error": null,
  "verdict": ""
}
```

### RQ07 — `malformed`

*Targeting:* body is a JSON array, not an object

```json
{
  "id": "RQ07",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ08 — `malformed`

*Targeting:* body is unparseable JSON

```json
{
  "id": "RQ08",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ09 — `malformed`

*Targeting:* body is empty

```json
{
  "id": "RQ09",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ10 — `malformed`

*Targeting:* body is form-encoded, not JSON

```json
{
  "id": "RQ10",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ11 — `malformed`

*Targeting:* body is JSON claiming to be plain text

```json
{
  "id": "RQ11",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ12 — `malformed`

*Targeting:* deeply nested JSON

```json
{
  "id": "RQ12",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ12",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_01 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_01",
  "status": 200,
  "content_id": "a1814614-808c-4d46-9cc9-4108223040b4",
  "creator_id": "attacker_flood",
  "guess": "unsure",
  "confidence": 0.0,
  "model_score": 0.0287,
  "style_score": 0.75,
  "label": "We can't tell whether this was written by a person or with AI help. That's common for plain or short writing, and it isn't an accusation. If you wrote this yourself and want a person to look at it, you can appeal.",
  "error": null,
  "verdict": ""
}
```

### FL01_02 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_02",
  "status": 200,
  "content_id": "dbc40a51-d0ae-4f68-bd09-ad46ad2dcc71",
  "creator_id": "attacker_flood",
  "guess": "unsure",
  "confidence": 0.0,
  "model_score": 0.0287,
  "style_score": 0.75,
  "label": "We can't tell whether this was written by a person or with AI help. That's common for plain or short writing, and it isn't an accusation. If you wrote this yourself and want a person to look at it, you can appeal.",
  "error": null,
  "verdict": ""
}
```

### FL01_03 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_03",
  "status": 200,
  "content_id": "af78d990-0350-4756-8b88-8583f55a1656",
  "creator_id": "attacker_flood",
  "guess": "unsure",
  "confidence": 0.0,
  "model_score": 0.0287,
  "style_score": 0.75,
  "label": "We can't tell whether this was written by a person or with AI help. That's common for plain or short writing, and it isn't an accusation. If you wrote this yourself and want a person to look at it, you can appeal.",
  "error": null,
  "verdict": ""
}
```

### FL01_04 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_04",
  "status": 200,
  "content_id": "77a0ee94-89b2-41b9-a9eb-a32511ce48e6",
  "creator_id": "attacker_flood",
  "guess": "unsure",
  "confidence": 0.0,
  "model_score": 0.0287,
  "style_score": 0.75,
  "label": "We can't tell whether this was written by a person or with AI help. That's common for plain or short writing, and it isn't an accusation. If you wrote this yourself and want a person to look at it, you can appeal.",
  "error": null,
  "verdict": ""
}
```

### FL01_05 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_05",
  "status": 200,
  "content_id": "6e6621c8-b1bc-4a92-8257-b7f717ff51e0",
  "creator_id": "attacker_flood",
  "guess": "unsure",
  "confidence": 0.0,
  "model_score": 0.0287,
  "style_score": 0.75,
  "label": "We can't tell whether this was written by a person or with AI help. That's common for plain or short writing, and it isn't an accusation. If you wrote this yourself and want a person to look at it, you can appeal.",
  "error": null,
  "verdict": ""
}
```

### FL01_06 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_06",
  "status": 200,
  "content_id": "05a1777d-c453-4d74-9866-d4fb62ac6de9",
  "creator_id": "attacker_flood",
  "guess": "unsure",
  "confidence": 0.0,
  "model_score": 0.0287,
  "style_score": 0.75,
  "label": "We can't tell whether this was written by a person or with AI help. That's common for plain or short writing, and it isn't an accusation. If you wrote this yourself and want a person to look at it, you can appeal.",
  "error": null,
  "verdict": ""
}
```

### FL01_07 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_07",
  "status": 200,
  "content_id": "d7594095-7918-4fb0-9b7d-3e4c493cd94e",
  "creator_id": "attacker_flood",
  "guess": "unsure",
  "confidence": 0.0,
  "model_score": 0.0287,
  "style_score": 0.75,
  "label": "We can't tell whether this was written by a person or with AI help. That's common for plain or short writing, and it isn't an accusation. If you wrote this yourself and want a person to look at it, you can appeal.",
  "error": null,
  "verdict": ""
}
```

### FL01_08 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_08",
  "status": 200,
  "content_id": "4c6c91d1-038c-439d-95df-95f82c407551",
  "creator_id": "attacker_flood",
  "guess": "unsure",
  "confidence": 0.0,
  "model_score": 0.0287,
  "style_score": 0.75,
  "label": "We can't tell whether this was written by a person or with AI help. That's common for plain or short writing, and it isn't an accusation. If you wrote this yourself and want a person to look at it, you can appeal.",
  "error": null,
  "verdict": ""
}
```

### FL01_09 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_09",
  "status": 200,
  "content_id": "7c3ec22a-eb87-4cf8-a7b2-68dcb91062cf",
  "creator_id": "attacker_flood",
  "guess": "unsure",
  "confidence": 0.0,
  "model_score": 0.0287,
  "style_score": 0.75,
  "label": "We can't tell whether this was written by a person or with AI help. That's common for plain or short writing, and it isn't an accusation. If you wrote this yourself and want a person to look at it, you can appeal.",
  "error": null,
  "verdict": ""
}
```

### FL01_10 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_10",
  "status": 200,
  "content_id": "4af63213-69af-41f6-9637-c08125733fff",
  "creator_id": "attacker_flood",
  "guess": "unsure",
  "confidence": 0.0,
  "model_score": 0.0287,
  "style_score": 0.75,
  "label": "We can't tell whether this was written by a person or with AI help. That's common for plain or short writing, and it isn't an accusation. If you wrote this yourself and want a person to look at it, you can appeal.",
  "error": null,
  "verdict": ""
}
```

### FL01_11 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_11",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_12 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_12",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```
