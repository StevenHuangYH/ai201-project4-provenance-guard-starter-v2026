# Run log — before

- Produced by: `run_eval.py::main`
- Service: `app.py::submit` · scoring: `scoring.py::combine_signals`
- 3 trials per criterion · 2026-11-11 02:35

Fill in Target from `criteria.md`, and Run and Verdict from the output
underneath. Whether a trial passed depends on the criterion you wrote.

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. my own writing |  |   |   |   |  |
| 2. plain writing |  |   |   |   |  |
| 3. clear ai |  |   |   |   |  |
| 3. clear human |  |   |   |   |  |
| 4. appeal path |  |   |   |   |  |
| 5. bad input |  |   |   |   |  |

---

## What actually came back

Real output. Paste the relevant parts into your README — the rubric
asks for the actual JSON, not a description of it.

### my own writing

**Trial 1**

```json
[
  {
    "status": null,
    "error": "ReadTimeout: HTTPConnectionPool(host='127.0.0.1', port=5000): Read timed out. (read timeout=90.0)",
    "sent": "When coffee was over, Colonel Fitzwilliam reminded Elizabeth of having"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.0,
    "model_score": 0.5241,
    "style_score": 0.4812,
    "combined_score": 0.5027,
    "label": "We can't tell whether this was written by a person or with AI help. That's common for plain or short writing, and it isn't an accusation. If you wrote this yourself and want a person to look at it, you can appeal.",
    "error": null,
    "elapsed_s": 35.742,
    "logged_as": [
      "decided"
    ],
    "sent": "Tom was evidently perturbed at Daisy\u2019s running around alone, for on th"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.0,
    "model_score": 0.5398,
    "style_score": 0.7083,
    "combined_score": 0.624,
    "label": "We can't tell whether this was written by a person or with AI help. That's common for plain or short writing, and it isn't an accusation. If you wrote this yourself and want a person to look at it, you can appeal.",
    "error": null,
    "elapsed_s": 0.294,
    "logged_as": [
      "decided"
    ],
    "sent": "He was a large man with rounded shoulders, a massive head, and a broad"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.0,
    "model_score": 0.4493,
    "style_score": 0.437,
    "combined_score": 0.4431,
    "label": "We can't tell whether this was written by a person or with AI help. That's common for plain or short writing, and it isn't an accusation. If you wrote this yourself and want a person to look at it, you can appeal.",
    "error": null,
    "elapsed_s": 0.25,
    "logged_as": [
      "decided"
    ],
    "sent": "So far there was no great harm. No lives were lost, and we could wade "
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.0,
    "model_score": 0.5529,
    "style_score": 0.316,
    "combined_score": 0.4345,
    "label": "We can't tell whether this was written by a person or with AI help. That's common for plain or short writing, and it isn't an accusation. If you wrote this yourself and want a person to look at it, you can appeal.",
    "error": null,
    "elapsed_s": 0.385,
    "logged_as": [
      "decided"
    ],
    "sent": "Dorian Gray drew a long breath. The colour came back to his cheeks, an"
  },
  {
    "status": 500,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "combined_score": null,
    "label": null,
    "error": "response was not JSON",
    "elapsed_s": 1.227,
    "logged_as": [],
    "sent": "It used, thought Clarissa, to be so simple. Down down through the air "
  },
  {
    "status": 500,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "combined_score": null,
    "label": null,
    "error": "response was not JSON",
    "elapsed_s": 0.192,
    "logged_as": [],
    "sent": "Miss Devlin had become Mrs Kearney out of spite. She had been educated"
  },
  {
    "status": 500,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "combined_score": null,
    "label": null,
    "error": "response was not JSON",
    "elapsed_s": 0.173,
    "logged_as": [],
    "sent": "I sailed from Baltimore for St. Michael\u2019s in the sloop Amanda, Captain"
  },
  {
    "status": 500,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "combined_score": null,
    "label": null,
    "error": "response was not JSON",
    "elapsed_s": 0.168,
    "logged_as": [],
    "sent": "Isabella ceased speaking, and took a drink of tea; then she rose, and "
  },
  {
    "status": 500,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "combined_score": null,
    "label": null,
    "error": "response was not JSON",
    "elapsed_s": 0.163,
    "logged_as": [],
    "sent": "She wanted to know if I was happy at Thornfield Hall, and what sort of"
  }
]
```

**Trial 2**

```json
[
  {
    "status": 500,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "combined_score": null,
    "label": null,
    "error": "response was not JSON",
    "elapsed_s": 0.165,
    "logged_as": [],
    "sent": "When coffee was over, Colonel Fitzwilliam reminded Elizabeth of having"
  },
  {
    "status": 500,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "combined_score": null,
    "label": null,
    "error": "response was not JSON",
    "elapsed_s": 0.187,
    "logged_as": [],
    "sent": "Tom was evidently perturbed at Daisy\u2019s running around alone, for on th"
  },
  {
    "status": 500,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "combined_score": null,
    "label": null,
    "error": "response was not JSON",
    "elapsed_s": 0.174,
    "logged_as": [],
    "sent": "He was a large man with rounded shoulders, a massive head, and a broad"
  },
  {
    "status": 500,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "combined_score": null,
    "label": null,
    "error": "response was not JSON",
    "elapsed_s": 0.181,
    "logged_as": [],
    "sent": "So far there was no great harm. No lives were lost, and we could wade "
  },
  {
    "status": 500,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "combined_score": null,
    "label": null,
    "error": "response was not JSON",
    "elapsed_s": 0.171,
    "logged_as": [],
    "sent": "Dorian Gray drew a long breath. The colour came back to his cheeks, an"
  },
  {
    "status": 500,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "combined_score": null,
    "label": null,
    "error": "response was not JSON",
    "elapsed_s": 0.175,
    "logged_as": [],
    "sent": "It used, thought Clarissa, to be so simple. Down down through the air "
  },
  {
    "status": 500,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "combined_score": null,
    "label": null,
    "error": "response was not JSON",
    "elapsed_s": 0.173,
    "logged_as": [],
    "sent": "Miss Devlin had become Mrs Kearney out of spite. She had been educated"
  },
  {
    "status": 500,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "combined_score": null,
    "label": null,
    "error": "response was not JSON",
    "elapsed_s": 0.173,
    "logged_as": [],
    "sent": "I sailed from Baltimore for St. Michael\u2019s in the sloop Amanda, Captain"
  },
  {
    "status": 500,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "combined_score": null,
    "label": null,
    "error": "response was not JSON",
    "elapsed_s": 0.179,
    "logged_as": [],
    "sent": "Isabella ceased speaking, and took a drink of tea; then she rose, and "
  },
  {
    "status": 500,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "combined_score": null,
    "label": null,
    "error": "response was not JSON",
    "elapsed_s": 0.165,
    "logged_as": [],
    "sent": "She wanted to know if I was happy at Thornfield Hall, and what sort of"
  }
]
```

**Trial 3**

```json
[
  {
    "status": 500,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "combined_score": null,
    "label": null,
    "error": "response was not JSON",
    "elapsed_s": 0.18,
    "logged_as": [],
    "sent": "When coffee was over, Colonel Fitzwilliam reminded Elizabeth of having"
  },
  {
    "status": 500,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "combined_score": null,
    "label": null,
    "error": "response was not JSON",
    "elapsed_s": 0.178,
    "logged_as": [],
    "sent": "Tom was evidently perturbed at Daisy\u2019s running around alone, for on th"
  },
  {
    "status": 500,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "combined_score": null,
    "label": null,
    "error": "response was not JSON",
    "elapsed_s": 0.182,
    "logged_as": [],
    "sent": "He was a large man with rounded shoulders, a massive head, and a broad"
  },
  {
    "status": 500,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "combined_score": null,
    "label": null,
    "error": "response was not JSON",
    "elapsed_s": 0.18,
    "logged_as": [],
    "sent": "So far there was no great harm. No lives were lost, and we could wade "
  },
  {
    "status": 500,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "combined_score": null,
    "label": null,
    "error": "response was not JSON",
    "elapsed_s": 0.212,
    "logged_as": [],
    "sent": "Dorian Gray drew a long breath. The colour came back to his cheeks, an"
  },
  {
    "status": 500,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "combined_score": null,
    "label": null,
    "error": "response was not JSON",
    "elapsed_s": 0.18,
    "logged_as": [],
    "sent": "It used, thought Clarissa, to be so simple. Down down through the air "
  },
  {
    "status": 500,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "combined_score": null,
    "label": null,
    "error": "response was not JSON",
    "elapsed_s": 0.168,
    "logged_as": [],
    "sent": "Miss Devlin had become Mrs Kearney out of spite. She had been educated"
  },
  {
    "status": 500,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "combined_score": null,
    "label": null,
    "error": "response was not JSON",
    "elapsed_s": 0.187,
    "logged_as": [],
    "sent": "I sailed from Baltimore for St. Michael\u2019s in the sloop Amanda, Captain"
  },
  {
    "status": 500,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "combined_score": null,
    "label": null,
    "error": "response was not JSON",
    "elapsed_s": 0.192,
    "logged_as": [],
    "sent": "Isabella ceased speaking, and took a drink of tea; then she rose, and "
  },
  {
    "status": 500,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "combined_score": null,
    "label": null,
    "error": "response was not JSON",
    "elapsed_s": 0.174,
    "logged_as": [],
    "sent": "She wanted to know if I was happy at Thornfield Hall, and what sort of"
  }
]
```

### plain writing

**Trial 1**

```json
[
  {
    "status": 500,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "combined_score": null,
    "label": null,
    "error": "response was not JSON",
    "elapsed_s": 0.196,
    "logged_as": [],
    "sent": "I moved to this city two years ago. At first it was hard for me. I did"
  },
  {
    "status": 500,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "combined_score": null,
    "label": null,
    "error": "response was not JSON",
    "elapsed_s": 0.193,
    "logged_as": [],
    "sent": "He was delighted with Italy. It was a beautiful country he said. The p"
  },
  {
    "status": 500,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "combined_score": null,
    "label": null,
    "error": "response was not JSON",
    "elapsed_s": 0.166,
    "logged_as": [],
    "sent": "We walked back down the road from Roncesvalles with Harris between us."
  },
  {
    "status": 500,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "combined_score": null,
    "label": null,
    "error": "response was not JSON",
    "elapsed_s": 0.17,
    "logged_as": [],
    "sent": "Jack doesn\u2019t say anything. He just sits there on the bed. He ain\u2019t wit"
  },
  {
    "status": 500,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "combined_score": null,
    "label": null,
    "error": "response was not JSON",
    "elapsed_s": 0.176,
    "logged_as": [],
    "sent": "The first time I ever saw the late Collis P. Huntington, the great rai"
  }
]
```

**Trial 2**

```json
[
  {
    "status": 500,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "combined_score": null,
    "label": null,
    "error": "response was not JSON",
    "elapsed_s": 0.169,
    "logged_as": [],
    "sent": "I moved to this city two years ago. At first it was hard for me. I did"
  },
  {
    "status": 500,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "combined_score": null,
    "label": null,
    "error": "response was not JSON",
    "elapsed_s": 0.171,
    "logged_as": [],
    "sent": "He was delighted with Italy. It was a beautiful country he said. The p"
  },
  {
    "status": 500,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "combined_score": null,
    "label": null,
    "error": "response was not JSON",
    "elapsed_s": 0.176,
    "logged_as": [],
    "sent": "We walked back down the road from Roncesvalles with Harris between us."
  },
  {
    "status": 500,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "combined_score": null,
    "label": null,
    "error": "response was not JSON",
    "elapsed_s": 0.175,
    "logged_as": [],
    "sent": "Jack doesn\u2019t say anything. He just sits there on the bed. He ain\u2019t wit"
  },
  {
    "status": 500,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "combined_score": null,
    "label": null,
    "error": "response was not JSON",
    "elapsed_s": 0.177,
    "logged_as": [],
    "sent": "The first time I ever saw the late Collis P. Huntington, the great rai"
  }
]
```

**Trial 3**

```json
[
  {
    "status": 500,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "combined_score": null,
    "label": null,
    "error": "response was not JSON",
    "elapsed_s": 0.181,
    "logged_as": [],
    "sent": "I moved to this city two years ago. At first it was hard for me. I did"
  },
  {
    "status": 500,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "combined_score": null,
    "label": null,
    "error": "response was not JSON",
    "elapsed_s": 0.191,
    "logged_as": [],
    "sent": "He was delighted with Italy. It was a beautiful country he said. The p"
  },
  {
    "status": 500,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "combined_score": null,
    "label": null,
    "error": "response was not JSON",
    "elapsed_s": 0.218,
    "logged_as": [],
    "sent": "We walked back down the road from Roncesvalles with Harris between us."
  },
  {
    "status": 500,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "combined_score": null,
    "label": null,
    "error": "response was not JSON",
    "elapsed_s": 0.182,
    "logged_as": [],
    "sent": "Jack doesn\u2019t say anything. He just sits there on the bed. He ain\u2019t wit"
  },
  {
    "status": 500,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "combined_score": null,
    "label": null,
    "error": "response was not JSON",
    "elapsed_s": 0.214,
    "logged_as": [],
    "sent": "The first time I ever saw the late Collis P. Huntington, the great rai"
  }
]
```

### clear ai

**Trial 1**

```json
[
  {
    "status": 500,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "combined_score": null,
    "label": null,
    "error": "response was not JSON",
    "elapsed_s": 0.167,
    "logged_as": [],
    "sent": "Time management is an essential skill that can significantly enhance b"
  },
  {
    "status": 500,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "combined_score": null,
    "label": null,
    "error": "response was not JSON",
    "elapsed_s": 0.172,
    "logged_as": [],
    "sent": "Climate change is one of the most pressing challenges facing our world"
  },
  {
    "status": 500,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "combined_score": null,
    "label": null,
    "error": "response was not JSON",
    "elapsed_s": 0.168,
    "logged_as": [],
    "sent": "Reading offers numerous benefits for individuals of all ages. It expan"
  },
  {
    "status": 500,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "combined_score": null,
    "label": null,
    "error": "response was not JSON",
    "elapsed_s": 0.176,
    "logged_as": [],
    "sent": "Artificial intelligence is transforming the way we live and work. From"
  },
  {
    "status": 500,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "combined_score": null,
    "label": null,
    "error": "response was not JSON",
    "elapsed_s": 0.174,
    "logged_as": [],
    "sent": "Regular exercise is a key component of a healthy lifestyle. It strengt"
  }
]
```

**Trial 2**

```json
[
  {
    "status": 500,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "combined_score": null,
    "label": null,
    "error": "response was not JSON",
    "elapsed_s": 0.182,
    "logged_as": [],
    "sent": "Time management is an essential skill that can significantly enhance b"
  },
  {
    "status": 500,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "combined_score": null,
    "label": null,
    "error": "response was not JSON",
    "elapsed_s": 0.182,
    "logged_as": [],
    "sent": "Climate change is one of the most pressing challenges facing our world"
  },
  {
    "status": 500,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "combined_score": null,
    "label": null,
    "error": "response was not JSON",
    "elapsed_s": 0.181,
    "logged_as": [],
    "sent": "Reading offers numerous benefits for individuals of all ages. It expan"
  },
  {
    "status": 500,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "combined_score": null,
    "label": null,
    "error": "response was not JSON",
    "elapsed_s": 0.196,
    "logged_as": [],
    "sent": "Artificial intelligence is transforming the way we live and work. From"
  },
  {
    "status": 500,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "combined_score": null,
    "label": null,
    "error": "response was not JSON",
    "elapsed_s": 0.205,
    "logged_as": [],
    "sent": "Regular exercise is a key component of a healthy lifestyle. It strengt"
  }
]
```

**Trial 3**

```json
[
  {
    "status": 500,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "combined_score": null,
    "label": null,
    "error": "response was not JSON",
    "elapsed_s": 0.195,
    "logged_as": [],
    "sent": "Time management is an essential skill that can significantly enhance b"
  },
  {
    "status": 500,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "combined_score": null,
    "label": null,
    "error": "response was not JSON",
    "elapsed_s": 0.173,
    "logged_as": [],
    "sent": "Climate change is one of the most pressing challenges facing our world"
  },
  {
    "status": 500,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "combined_score": null,
    "label": null,
    "error": "response was not JSON",
    "elapsed_s": 0.172,
    "logged_as": [],
    "sent": "Reading offers numerous benefits for individuals of all ages. It expan"
  },
  {
    "status": 500,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "combined_score": null,
    "label": null,
    "error": "response was not JSON",
    "elapsed_s": 0.165,
    "logged_as": [],
    "sent": "Artificial intelligence is transforming the way we live and work. From"
  },
  {
    "status": 500,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "combined_score": null,
    "label": null,
    "error": "response was not JSON",
    "elapsed_s": 0.169,
    "logged_as": [],
    "sent": "Regular exercise is a key component of a healthy lifestyle. It strengt"
  }
]
```

### clear human

**Trial 1**

```json
[
  {
    "status": 500,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "combined_score": null,
    "label": null,
    "error": "response was not JSON",
    "elapsed_s": 0.172,
    "logged_as": [],
    "sent": "I went to the woods because I wished to live deliberately, to front on"
  },
  {
    "status": 500,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "combined_score": null,
    "label": null,
    "error": "response was not JSON",
    "elapsed_s": 0.169,
    "logged_as": [],
    "sent": "You don't know about me without you have read a book by the name of Th"
  },
  {
    "status": 500,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "combined_score": null,
    "label": null,
    "error": "response was not JSON",
    "elapsed_s": 0.183,
    "logged_as": [],
    "sent": "Call me Ishmael. Some years ago, never mind how long precisely, having"
  },
  {
    "status": 500,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "combined_score": null,
    "label": null,
    "error": "response was not JSON",
    "elapsed_s": 0.186,
    "logged_as": [],
    "sent": "It was the best of times, it was the worst of times, it was the age of"
  },
  {
    "status": 500,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "combined_score": null,
    "label": null,
    "error": "response was not JSON",
    "elapsed_s": 0.173,
    "logged_as": [],
    "sent": "There were four of us, George, and William Samuel Harris, and myself, "
  }
]
```

**Trial 2**

```json
[
  {
    "status": 500,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "combined_score": null,
    "label": null,
    "error": "response was not JSON",
    "elapsed_s": 0.208,
    "logged_as": [],
    "sent": "I went to the woods because I wished to live deliberately, to front on"
  },
  {
    "status": 500,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "combined_score": null,
    "label": null,
    "error": "response was not JSON",
    "elapsed_s": 0.182,
    "logged_as": [],
    "sent": "You don't know about me without you have read a book by the name of Th"
  },
  {
    "status": 500,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "combined_score": null,
    "label": null,
    "error": "response was not JSON",
    "elapsed_s": 0.178,
    "logged_as": [],
    "sent": "Call me Ishmael. Some years ago, never mind how long precisely, having"
  },
  {
    "status": 500,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "combined_score": null,
    "label": null,
    "error": "response was not JSON",
    "elapsed_s": 0.176,
    "logged_as": [],
    "sent": "It was the best of times, it was the worst of times, it was the age of"
  },
  {
    "status": 500,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "combined_score": null,
    "label": null,
    "error": "response was not JSON",
    "elapsed_s": 0.172,
    "logged_as": [],
    "sent": "There were four of us, George, and William Samuel Harris, and myself, "
  }
]
```

**Trial 3**

```json
[
  {
    "status": 500,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "combined_score": null,
    "label": null,
    "error": "response was not JSON",
    "elapsed_s": 0.171,
    "logged_as": [],
    "sent": "I went to the woods because I wished to live deliberately, to front on"
  },
  {
    "status": 500,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "combined_score": null,
    "label": null,
    "error": "response was not JSON",
    "elapsed_s": 0.17,
    "logged_as": [],
    "sent": "You don't know about me without you have read a book by the name of Th"
  },
  {
    "status": 500,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "combined_score": null,
    "label": null,
    "error": "response was not JSON",
    "elapsed_s": 0.195,
    "logged_as": [],
    "sent": "Call me Ishmael. Some years ago, never mind how long precisely, having"
  },
  {
    "status": 500,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "combined_score": null,
    "label": null,
    "error": "response was not JSON",
    "elapsed_s": 0.202,
    "logged_as": [],
    "sent": "It was the best of times, it was the worst of times, it was the age of"
  },
  {
    "status": 500,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "combined_score": null,
    "label": null,
    "error": "response was not JSON",
    "elapsed_s": 0.19,
    "logged_as": [],
    "sent": "There were four of us, George, and William Samuel Harris, and myself, "
  }
]
```

### appeal path

**Trial 1**

```json
[
  {
    "kind": "real",
    "submit_status": 500,
    "content_id": null,
    "appeal_status": 400,
    "log_statuses": [
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected"
    ]
  },
  {
    "kind": "real",
    "submit_status": 500,
    "content_id": null,
    "appeal_status": 400,
    "log_statuses": [
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected"
    ]
  },
  {
    "kind": "real",
    "submit_status": 500,
    "content_id": null,
    "appeal_status": 400,
    "log_statuses": [
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected"
    ]
  },
  {
    "kind": "real",
    "submit_status": 500,
    "content_id": null,
    "appeal_status": 400,
    "log_statuses": [
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected"
    ]
  },
  {
    "kind": "real",
    "submit_status": 500,
    "content_id": null,
    "appeal_status": 400,
    "log_statuses": [
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected"
    ]
  },
  {
    "kind": "bogus",
    "content_id": "does-not-exist-t1",
    "appeal_status": 404,
    "log_statuses": []
  },
  {
    "kind": "bogus",
    "content_id": "00000000-0000-0000-0000-000000000000-t1",
    "appeal_status": 404,
    "log_statuses": []
  },
  {
    "kind": "bogus",
    "content_id": "typo-cb0a0967-t1",
    "appeal_status": 404,
    "log_statuses": []
  }
]
```

**Trial 2**

```json
[
  {
    "kind": "real",
    "submit_status": 500,
    "content_id": null,
    "appeal_status": 400,
    "log_statuses": [
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected"
    ]
  },
  {
    "kind": "real",
    "submit_status": 500,
    "content_id": null,
    "appeal_status": 400,
    "log_statuses": [
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected"
    ]
  },
  {
    "kind": "real",
    "submit_status": 500,
    "content_id": null,
    "appeal_status": 400,
    "log_statuses": [
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected"
    ]
  },
  {
    "kind": "real",
    "submit_status": 500,
    "content_id": null,
    "appeal_status": 400,
    "log_statuses": [
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected"
    ]
  },
  {
    "kind": "real",
    "submit_status": 500,
    "content_id": null,
    "appeal_status": 400,
    "log_statuses": [
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected"
    ]
  },
  {
    "kind": "bogus",
    "content_id": "does-not-exist-t2",
    "appeal_status": 404,
    "log_statuses": []
  },
  {
    "kind": "bogus",
    "content_id": "00000000-0000-0000-0000-000000000000-t2",
    "appeal_status": 404,
    "log_statuses": []
  },
  {
    "kind": "bogus",
    "content_id": "typo-cb0a0967-t2",
    "appeal_status": 404,
    "log_statuses": []
  }
]
```

**Trial 3**

```json
[
  {
    "kind": "real",
    "submit_status": 500,
    "content_id": null,
    "appeal_status": 400,
    "log_statuses": [
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected"
    ]
  },
  {
    "kind": "real",
    "submit_status": 500,
    "content_id": null,
    "appeal_status": 400,
    "log_statuses": [
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected"
    ]
  },
  {
    "kind": "real",
    "submit_status": 500,
    "content_id": null,
    "appeal_status": 400,
    "log_statuses": [
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected"
    ]
  },
  {
    "kind": "real",
    "submit_status": 500,
    "content_id": null,
    "appeal_status": 400,
    "log_statuses": [
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected"
    ]
  },
  {
    "kind": "real",
    "submit_status": 500,
    "content_id": null,
    "appeal_status": 400,
    "log_statuses": [
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected",
      "rejected"
    ]
  },
  {
    "kind": "bogus",
    "content_id": "does-not-exist-t3",
    "appeal_status": 404,
    "log_statuses": []
  },
  {
    "kind": "bogus",
    "content_id": "00000000-0000-0000-0000-000000000000-t3",
    "appeal_status": 404,
    "log_statuses": []
  },
  {
    "kind": "bogus",
    "content_id": "typo-cb0a0967-t3",
    "appeal_status": 404,
    "log_statuses": []
  }
]
```

### bad input

**Trial 1**

```json
[
  {
    "status": 400,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "combined_score": null,
    "label": null,
    "error": "missing_text",
    "elapsed_s": 0.008,
    "logged_as": [
      "rejected"
    ],
    "sent": "(empty text)"
  },
  {
    "status": 400,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "combined_score": null,
    "label": null,
    "error": "missing_text",
    "elapsed_s": 0.008,
    "logged_as": [
      "rejected"
    ],
    "sent": "{\"creator_id\": \"eval_bad_missing\"}"
  },
  {
    "status": 400,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "combined_score": null,
    "label": null,
    "error": "missing_text",
    "elapsed_s": 0.008,
    "logged_as": [
      "rejected"
    ],
    "sent": "{\"text\": null, \"creator_id\": \"eval_bad_null\"}"
  },
  {
    "status": 413,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "combined_score": null,
    "label": null,
    "error": "text_too_long",
    "elapsed_s": 0.011,
    "logged_as": [
      "rejected"
    ],
    "sent": "word word word word word word word word word word word word word word "
  }
]
```

**Trial 2**

```json
[
  {
    "status": 400,
    "guess": null,
    "confidence": null,
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
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "combined_score": null,
    "label": null,
    "error": "missing_text",
    "elapsed_s": 0.009,
    "logged_as": [
      "rejected"
    ],
    "sent": "{\"creator_id\": \"eval_bad_missing\"}"
  },
  {
    "status": 400,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "combined_score": null,
    "label": null,
    "error": "missing_text",
    "elapsed_s": 0.008,
    "logged_as": [
      "rejected"
    ],
    "sent": "{\"text\": null, \"creator_id\": \"eval_bad_null\"}"
  },
  {
    "status": 413,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "combined_score": null,
    "label": null,
    "error": "text_too_long",
    "elapsed_s": 0.01,
    "logged_as": [
      "rejected"
    ],
    "sent": "word word word word word word word word word word word word word word "
  }
]
```

**Trial 3**

```json
[
  {
    "status": 400,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "combined_score": null,
    "label": null,
    "error": "missing_text",
    "elapsed_s": 0.008,
    "logged_as": [
      "rejected"
    ],
    "sent": "(empty text)"
  },
  {
    "status": 400,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "combined_score": null,
    "label": null,
    "error": "missing_text",
    "elapsed_s": 0.008,
    "logged_as": [
      "rejected"
    ],
    "sent": "{\"creator_id\": \"eval_bad_missing\"}"
  },
  {
    "status": 400,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "combined_score": null,
    "label": null,
    "error": "missing_text",
    "elapsed_s": 0.008,
    "logged_as": [
      "rejected"
    ],
    "sent": "{\"text\": null, \"creator_id\": \"eval_bad_null\"}"
  },
  {
    "status": 413,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "combined_score": null,
    "label": null,
    "error": "text_too_long",
    "elapsed_s": 0.009,
    "logged_as": [
      "rejected"
    ],
    "sent": "word word word word word word word word word word word word word word "
  }
]
```
