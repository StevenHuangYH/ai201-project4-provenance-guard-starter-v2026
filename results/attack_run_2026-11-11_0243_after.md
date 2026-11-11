# Attack run — after

- Produced by: `run_attacks.py::main`
- Service: `app.py::submit`
- 56 attacks · 2026-11-11 02:43
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
| EV01 | evasion | signal two: typos raise word variety | 200 | `caf4da87-eb13-4d88-842c-57ed01a18f15` | unsure | 0.000 |  |
| EV02 | evasion | signal two: broken-up sentences raise length spread | 200 | `ea7fad8a-507c-4d7c-99d2-ddb2a77ba68e` | unsure | 0.000 |  |
| EV03 | evasion | signal two: a pasted quotation changes the shape | 200 | `6adbde04-2190-4b8e-9181-0cb7da085afa` | unsure | 0.000 |  |
| EV04 | evasion | signal one: unusual words raise perplexity | 200 | `997afe3f-520f-4809-9a45-3e39f4c1eaae` | unsure | 0.000 |  |
| EV05 | evasion | both signals: heavy human editing pass | 200 | `e0602d77-9581-4608-a47e-6a86c55d61ed` | human | 0.251 |  |
| EV06 | evasion | signal two: one very long sentence and one very short | 200 | `ef11d239-df51-4f10-8815-adab6d6f07d1` | unsure | 0.000 |  |
| EV07 | evasion | signal two: padding with punctuation | 200 | `17b07141-a9fb-4932-b958-3fdf82f9d790` | human | 0.156 |  |
| EV08 | evasion | signal one: text below the token window | 200 | `5ced64be-3111-4c84-a141-d0e9d1107540` | unsure | 0.000 |  |
| EV09 | evasion | both: AI text with a human opening paragraph bolted on | 200 | `2ad3d0bd-2c1e-4fbb-88df-5875ff2afce7` | unsure | 0.000 |  |
| EV10 | evasion | signal two: repeated stanza structure | 200 | `de1571a8-5fe0-4152-bb3b-d9b9a8d9ff10` | ai | 0.282 |  |
| FP01 | false_positive | plain, clear human writing with no flourishes | 200 | `3d18e342-394a-4dd1-bf58-3d3df606da67` | unsure | 0.000 |  |
| FP02 | false_positive | human writing in a formal register | 200 | `39335070-636f-4670-93bf-638a6e5522b4` | unsure | 0.000 |  |
| FP03 | false_positive | a non-native English speaker writing carefully | 200 | `b8e50ad1-4f76-4d0f-aab1-7607d7ee1d41` | unsure | 0.000 |  |
| FP04 | false_positive | a student essay written to a rubric | 200 | `dae7abc9-fc60-4be8-a79b-7211961de0ae` | unsure | 0.000 |  |
| FP05 | false_positive | technical documentation written by a person | 200 | `48b717b0-140b-4b8f-9a4d-3773472009ef` | ai | 0.130 |  |
| FP06 | false_positive | a person imitating a formal template | 200 | `f4730550-e80b-49fc-96ee-71bddfb426ae` | unsure | 0.000 |  |
| FP07 | false_positive | human writing that repeats a phrase deliberately | 200 | `20e5e23e-e83b-4e58-bf1c-5331a104ad8c` | unsure | 0.000 |  |
| FP08 | false_positive | very short genuine human submission | 200 | `f6f5fead-a911-49e1-a115-f8c77bc143db` | unsure | 0.000 |  |
| PI01 | prompt_injection | instruction to ignore the check | 200 | `e12908ab-3493-4f5a-89a9-f315bea29c4c` | unsure | 0.000 |  |
| PI02 | prompt_injection | instruction disguised as a system message | 200 | `3a8cc175-2e83-4048-99a6-bcb4eb20898d` | human | 0.221 |  |
| PI03 | prompt_injection | instruction wrapped in the writer's voice | 200 | `00d7ad11-4a0a-4c7a-8180-cfb8633305bc` | unsure | 0.000 |  |
| PI04 | prompt_injection | attempt to make the label text hostile | 200 | `325b7119-8ee2-4067-a281-4ab1cf6e5d3a` | unsure | 0.000 |  |
| PI05 | prompt_injection | attempt to inject into the audit log | 200 | `c9fec06e-0709-4e39-9334-0e62be6a6f1b` | unsure | 0.000 |  |
| PI06 | prompt_injection | instruction plus real human text | 200 | `480df3bf-4729-4b63-9df2-c24f10c1ea64` | unsure | 0.000 |  |
| MF01 | malformed | text is only whitespace | 400 | `—` | — | — |  |
| MF02 | malformed | text is a single character | 400 | `—` | — | — |  |
| MF03 | malformed | text is control characters | 200 | `74f412a7-b430-42d0-b889-d0d1c0ff8e0f` | unsure | 0.000 |  |
| MF04 | malformed | text is only punctuation | 200 | `19deb800-cb7a-4b4e-ab63-075d542c8498` | unsure | 0.000 |  |
| MF05 | malformed | text is a very long single word | 200 | `38165eed-e312-4759-93a4-cb2ff7354e63` | ai | 0.369 |  |
| MF06 | malformed | text is emoji only | 200 | `7d14c953-7143-498c-95ed-e163258e2630` | ai | 0.993 |  |
| MF07 | malformed | text is right-to-left script | 200 | `a401e26e-f9a2-4d32-b537-308e86101545` | ai | 0.766 |  |
| MF08 | malformed | text is 60,000 characters | 413 | `—` | — | — |  |
| RQ01 | malformed | no text field at all | 400 | `—` | — | — |  |
| RQ02 | malformed | no creator_id | 200 | `e5228db6-737c-40e2-8e60-58ccfc66babb` | unsure | 0.000 |  |
| RQ03 | malformed | text is a number | 400 | `—` | — | — |  |
| RQ04 | malformed | text is a list | 400 | `—` | — | — |  |
| RQ05 | malformed | text is null | 400 | `—` | — | — |  |
| RQ06 | malformed | creator_id is an object | 200 | `98f34ac3-ec3e-435c-9772-1ad73750070a` | unsure | 0.000 |  |
| RQ07 | malformed | body is a JSON array, not an object | 400 | `—` | — | — |  |
| RQ08 | malformed | body is unparseable JSON | 400 | `—` | — | — |  |
| RQ09 | malformed | body is empty | 400 | `—` | — | — |  |
| RQ10 | malformed | body is form-encoded, not JSON | 400 | `—` | — | — |  |
| RQ11 | malformed | body is JSON claiming to be plain text | 400 | `—` | — | — |  |
| RQ12 | malformed | deeply nested JSON | 400 | `—` | — | — |  |
| FL01_01 | flood_same_creator | 20 rapid submissions from one creator | 200 | `1efe1137-fa02-4a0f-802c-e0f14140952e` | unsure | 0.000 |  |
| FL01_02 | flood_same_creator | 20 rapid submissions from one creator | 200 | `46c90c8b-3b1f-4501-8cbc-f180dd3a7653` | unsure | 0.000 |  |
| FL01_03 | flood_same_creator | 20 rapid submissions from one creator | 200 | `97930f77-8f39-4c4a-a13a-d219e4d4b536` | unsure | 0.000 |  |
| FL01_04 | flood_same_creator | 20 rapid submissions from one creator | 200 | `4e518280-0dd5-437a-969c-5a86393e2c2d` | unsure | 0.000 |  |
| FL01_05 | flood_same_creator | 20 rapid submissions from one creator | 200 | `7d5932c6-0a2e-4200-8e87-7b9f043a17bd` | unsure | 0.000 |  |
| FL01_06 | flood_same_creator | 20 rapid submissions from one creator | 200 | `7b0b620d-6f20-425a-b967-3b803683ea85` | unsure | 0.000 |  |
| FL01_07 | flood_same_creator | 20 rapid submissions from one creator | 200 | `f6495456-fa9f-4c1c-b10d-a15e1f121eb8` | unsure | 0.000 |  |
| FL01_08 | flood_same_creator | 20 rapid submissions from one creator | 200 | `e4084a56-33bb-4c96-9a67-f0923d01955b` | unsure | 0.000 |  |
| FL01_09 | flood_same_creator | 20 rapid submissions from one creator | 200 | `6c3b1079-419a-4585-8db7-c221b7cd8542` | unsure | 0.000 |  |
| FL01_10 | flood_same_creator | 20 rapid submissions from one creator | 200 | `fb7e8d91-057b-49c5-a8a4-6af279fe66df` | unsure | 0.000 |  |
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
  "content_id": "caf4da87-eb13-4d88-842c-57ed01a18f15",
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
  "content_id": "ea7fad8a-507c-4d7c-99d2-ddb2a77ba68e",
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
  "content_id": "6adbde04-2190-4b8e-9181-0cb7da085afa",
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
  "content_id": "997afe3f-520f-4809-9a45-3e39f4c1eaae",
  "creator_id": "attacker_EV04",
  "guess": "unsure",
  "confidence": 0.0,
  "model_score": 0.6114,
  "style_score": 0.8245,
  "label": "We can't tell whether this was written by a person or with AI help. That's common for plain or short writing, and it isn't an accusation. If you wrote this yourself and want a person to look at it, you can appeal.",
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
  "content_id": "e0602d77-9581-4608-a47e-6a86c55d61ed",
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
  "content_id": "ef11d239-df51-4f10-8815-adab6d6f07d1",
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
  "content_id": "17b07141-a9fb-4932-b958-3fdf82f9d790",
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
  "content_id": "5ced64be-3111-4c84-a141-d0e9d1107540",
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
  "content_id": "2ad3d0bd-2c1e-4fbb-88df-5875ff2afce7",
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
  "content_id": "de1571a8-5fe0-4152-bb3b-d9b9a8d9ff10",
  "creator_id": "attacker_EV10",
  "guess": "ai",
  "confidence": 0.2825,
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
  "content_id": "3d18e342-394a-4dd1-bf58-3d3df606da67",
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
  "content_id": "39335070-636f-4670-93bf-638a6e5522b4",
  "creator_id": "attacker_FP02",
  "guess": "unsure",
  "confidence": 0.0,
  "model_score": 0.7387,
  "style_score": 0.8337,
  "label": "We can't tell whether this was written by a person or with AI help. That's common for plain or short writing, and it isn't an accusation. If you wrote this yourself and want a person to look at it, you can appeal.",
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
  "content_id": "b8e50ad1-4f76-4d0f-aab1-7607d7ee1d41",
  "creator_id": "attacker_FP03",
  "guess": "unsure",
  "confidence": 0.0,
  "model_score": 0.8051,
  "style_score": 0.7178,
  "label": "We can't tell whether this was written by a person or with AI help. That's common for plain or short writing, and it isn't an accusation. If you wrote this yourself and want a person to look at it, you can appeal.",
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
  "content_id": "dae7abc9-fc60-4be8-a79b-7211961de0ae",
  "creator_id": "attacker_FP04",
  "guess": "unsure",
  "confidence": 0.0,
  "model_score": 0.8329,
  "style_score": 0.6752,
  "label": "We can't tell whether this was written by a person or with AI help. That's common for plain or short writing, and it isn't an accusation. If you wrote this yourself and want a person to look at it, you can appeal.",
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
  "content_id": "48b717b0-140b-4b8f-9a4d-3773472009ef",
  "creator_id": "attacker_FP05",
  "guess": "ai",
  "confidence": 0.1295,
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
  "content_id": "f4730550-e80b-49fc-96ee-71bddfb426ae",
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
  "content_id": "20e5e23e-e83b-4e58-bf1c-5331a104ad8c",
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
  "content_id": "f6f5fead-a911-49e1-a115-f8c77bc143db",
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
  "content_id": "e12908ab-3493-4f5a-89a9-f315bea29c4c",
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
  "content_id": "3a8cc175-2e83-4048-99a6-bcb4eb20898d",
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
  "content_id": "00d7ad11-4a0a-4c7a-8180-cfb8633305bc",
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
  "content_id": "325b7119-8ee2-4067-a281-4ab1cf6e5d3a",
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
  "content_id": "c9fec06e-0709-4e39-9334-0e62be6a6f1b",
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
  "content_id": "480df3bf-4729-4b63-9df2-c24f10c1ea64",
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
  "content_id": "74f412a7-b430-42d0-b889-d0d1c0ff8e0f",
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
  "content_id": "19deb800-cb7a-4b4e-ab63-075d542c8498",
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
  "content_id": "38165eed-e312-4759-93a4-cb2ff7354e63",
  "creator_id": "attacker_MF05",
  "guess": "ai",
  "confidence": 0.369,
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
  "content_id": "7d14c953-7143-498c-95ed-e163258e2630",
  "creator_id": "attacker_MF06",
  "guess": "ai",
  "confidence": 0.9925,
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
  "content_id": "a401e26e-f9a2-4d32-b537-308e86101545",
  "creator_id": "attacker_MF07",
  "guess": "ai",
  "confidence": 0.766,
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
  "content_id": "e5228db6-737c-40e2-8e60-58ccfc66babb",
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
  "content_id": "98f34ac3-ec3e-435c-9772-1ad73750070a",
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
  "content_id": "1efe1137-fa02-4a0f-802c-e0f14140952e",
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
  "content_id": "46c90c8b-3b1f-4501-8cbc-f180dd3a7653",
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
  "content_id": "97930f77-8f39-4c4a-a13a-d219e4d4b536",
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
  "content_id": "4e518280-0dd5-437a-969c-5a86393e2c2d",
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
  "content_id": "7d5932c6-0a2e-4200-8e87-7b9f043a17bd",
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
  "content_id": "7b0b620d-6f20-425a-b967-3b803683ea85",
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
  "content_id": "f6495456-fa9f-4c1c-b10d-a15e1f121eb8",
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
  "content_id": "e4084a56-33bb-4c96-9a67-f0923d01955b",
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
  "content_id": "6c3b1079-419a-4585-8db7-c221b7cd8542",
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
  "content_id": "fb7e8d91-057b-49c5-a8a4-6af279fe66df",
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
