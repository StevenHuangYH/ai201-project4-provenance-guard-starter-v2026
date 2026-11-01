"""
Signal two: the style signal. ← YOU BUILD THIS IN MILESTONE 4

Signal one reads the text for meaning. This one measures it *as text* — the
shape of it, without understanding a word.

Three measures are stubbed below because the brief names those three. They are
stubs, not implementations: what they compute is yours, and so is how you
combine them.

    sentence_length_spread   do sentences vary in length, or march in step?
    type_token_ratio         how much of the vocabulary repeats?
    punctuation_density      how much punctuation, and how varied?

Why these might differ between human and AI writing: generated prose tends
toward even, mid-length sentences and a narrower band of vocabulary, because
that's what "most likely next word" produces on average. Human writing is
lumpier — a three-word sentence next to a forty-word one.

⚠️ **The blind spot, which you have to name in Milestone 1.**

This signal cannot read. It has no idea what the text says. Anything that
changes the shape without changing the substance moves it — adding typos,
breaking up sentences, pasting in a quotation. That is a very cheap thing for
someone to do on purpose, and unit 8's attack set will do it to you.

Build each function on its own and call it from a terminal before you wire
anything together:

    python stylometry.py "some text to look at"
"""

import re
import statistics


def sentences(text: str) -> list[str]:
    """Split into sentences. Rough and good enough — given to you."""
    parts = re.split(r"(?<=[.!?])\s+", text.strip())
    return [p for p in parts if p.strip()]


def words(text: str) -> list[str]:
    """Split into lowercase words, punctuation stripped. Given to you."""
    return re.findall(r"[a-z0-9']+", text.lower())


# ── The three measures — YOU BUILD THESE ─────────────────────────────────────

TTR_WINDOW = 50  # words per window for the moving type-token ratio

# Punctuation that varies between writers. Full stops are left out: nearly
# every sentence has exactly one, so counting them mostly counts sentences.
EXPRESSIVE_PUNCTUATION = set(",;:!?()\"'-—–…")


def sentence_length_spread(text: str) -> float:
    """
    How much sentence length varies, as a coefficient of variation.

    Returns:
        stdev of words-per-sentence divided by the mean. 0.0 means every
        sentence is the same length; around 0.6+ is lumpy, human-looking
        prose. **Higher means more human.**

        Fewer than two sentences returns 0.0 — there's no spread to measure.
        `style_signal` treats that case as "no evidence" rather than as AI,
        so a one-sentence submission isn't punished for being short.
    """
    lengths = [len(words(s)) for s in sentences(text)]
    lengths = [n for n in lengths if n > 0]
    if len(lengths) < 2:
        return 0.0
    mean = statistics.mean(lengths)
    return round(statistics.stdev(lengths) / mean, 4)


def type_token_ratio(text: str) -> float:
    """
    Unique words over total words, averaged over a sliding window.

    Returns:
        A float between 0 and 1. **Higher means more varied vocabulary.**

    Plain TTR falls as text gets longer, so a long human essay would look
    more repetitive than a short AI paragraph for no reason but length. This
    uses the moving-average version (MATTR): the TTR of every 50-word window,
    averaged. Texts shorter than one window fall back to plain TTR.
    """
    toks = words(text)
    if not toks:
        return 0.0
    if len(toks) <= TTR_WINDOW:
        return round(len(set(toks)) / len(toks), 4)
    ratios = [
        len(set(toks[i:i + TTR_WINDOW])) / TTR_WINDOW
        for i in range(len(toks) - TTR_WINDOW + 1)
    ]
    return round(statistics.mean(ratios), 4)


def punctuation_density(text: str) -> float:
    """
    Expressive punctuation marks per word.

    Returns:
        Count of commas, semicolons, colons, dashes, brackets, quotes,
        question and exclamation marks, divided by the word count. Typical
        prose lands between 0.05 and 0.25. **Higher means more human** — see
        `style_signal` for why that's the weakest of the three assumptions.
    """
    toks = words(text)
    if not toks:
        return 0.0
    marks = sum(1 for ch in text if ch in EXPRESSIVE_PUNCTUATION)
    # An apostrophe inside a word ("don't") is spelling, not punctuation.
    marks -= len(re.findall(r"[a-z0-9]'[a-z]", text.lower()))
    return round(max(marks, 0) / len(toks), 4)


# ── Combining them ───────────────────────────────────────────────────────────

def style_signal(text: str) -> float:
    """
    The style signal as a 0–1 score. **Higher means more likely AI.** ← TODO

    Combine your three measures into one number. Same direction as
    `detector.model_signal`, so that `scoring.combine_signals` can treat them
    the same way — if one of your signals runs backwards, everything above it
    is wrong in a way that's hard to see.

    Two things to decide and write down:

      1. Which direction each measure points. Low spread means more AI-ish, so
         it needs flipping. Work out which of your three need that.
      2. How to get each onto a comparable scale. A raw type-token ratio sits
         between 0 and 1; a raw punctuation count doesn't. Adding them
         unscaled means whichever has the bigger numbers wins by default.

    Test it on the four calibration inputs from Milestone 4 — clearly AI,
    clearly human, plain conventional human writing, lightly-edited AI — before
    you trust it. Plain and ordinary, not formal: formal prose reads as *human*
    to signal one, and it is plain writing that gets accused.

    How this one does it:

      1. Each measure is mapped onto 0–1 "human-ness" with a straight line
         between an AI-ish and a human-ish reference value (the ranges in
         STYLE_RANGES, set from the calibration inputs), clamped at the ends.
      2. The three are averaged with weights — spread counts most, type-token
         ratio least — and flipped, so the result is AI-ness.

    A one-sentence submission has no spread, so that measure drops out and
    the other two carry the score.
    """
    measures = {
        "spread": sentence_length_spread(text),
        "ttr": type_token_ratio(text),
        "punct": punctuation_density(text),
    }
    if len(sentences(text)) < 2:
        measures.pop("spread")

    total_weight = sum(STYLE_WEIGHTS[k] for k in measures)
    humanness = sum(
        STYLE_WEIGHTS[k] * _scale(value, *STYLE_RANGES[k])
        for k, value in measures.items()
    ) / total_weight
    return round(1.0 - humanness, 4)


# (AI-ish value, human-ish value) for each measure. Below the first scores 0
# human-ness, above the second scores 1, and in between is a straight line.
STYLE_RANGES = {
    "spread": (0.15, 0.70),
    "ttr": (0.60, 0.85),
    "punct": (0.04, 0.15),
}

# Spread separated the calibration inputs cleanly (AI 0.10–0.17, human
# 0.70–0.74). Type-token ratio pointed the WRONG way on paragraph-length text —
# the AI paragraphs had the most varied vocabulary — so it barely counts.
STYLE_WEIGHTS = {"spread": 0.6, "ttr": 0.1, "punct": 0.3}


def _scale(value: float, low: float, high: float) -> float:
    """Map `value` onto 0–1 between `low` and `high`, clamped."""
    return min(max((value - low) / (high - low), 0.0), 1.0)


if __name__ == "__main__":
    import sys

    text = " ".join(sys.argv[1:]) or (
        "The system works well. It handles most cases correctly and provides "
        "good results. Users generally find it easy to use and understand."
    )

    print(f"{len(sentences(text))} sentences, {len(words(text))} words\n")
    print(f"sentence_length_spread   {sentence_length_spread(text)}")
    print(f"type_token_ratio         {type_token_ratio(text)}")
    print(f"punctuation_density      {punctuation_density(text)}")
    print(f"style_signal             {style_signal(text)}   (higher = more likely AI)")
