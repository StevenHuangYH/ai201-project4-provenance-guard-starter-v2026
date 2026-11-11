#!/usr/bin/env python3
"""
Run your five criteria three times each.  <- UNIT 8, MILESTONE 3

    python app.py                              # in one terminal
    python run_eval.py --label before          # in another
    python run_eval.py --label after

The attack set tests what staff thought to test. This tests what *you* thought
to test, and the two rarely overlap much. Both count.

Fill in `scenarios.py` first — that's where you say what each criterion needs
run against it. A criterion about false positives needs your own writing. One
about label coverage needs inputs across the score range.

!! Three trials, and **your first signal runs a model, so identical input can
score differently twice.** That's exactly why repeats matter here.

This does the sending and the recording. It does not decide whether a trial
passed — that depends on the criterion you wrote, so the Verdict column comes
back blank.
"""

import argparse
import datetime as dt
import json
import sys
import time
from pathlib import Path

import config

# Windows consoles often run a codepage that can't print every character in
# this file's help text. Without this, `--help` ends in a UnicodeEncodeError
# traceback instead of the help — which is a miserable first thing to hit.
for _stream in (sys.stdout, sys.stderr):
    try:
        _stream.reconfigure(errors="replace")
    except (AttributeError, ValueError):  # not a normal text stream
        pass


DEFAULT_URL = f"http://{config.HOST}:{config.PORT}"


def bodies_for(scenario):
    """
    The request bodies one scenario sends.

    A "texts" scenario gets a creator_id made up for it. A "bodies" scenario is
    sent exactly as written, which is how a bad-input criterion says things a
    string can't — no `text` field, a null, something enormous.
    """
    if scenario.get("bodies"):
        return list(scenario["bodies"])
    return [
        {"text": text, "creator_id": f"eval_{scenario['name'][:12]}_{i}"}
        for i, text in enumerate(scenario["texts"], 1)
    ]


def describe(body):
    """A short, readable note of what was sent — for the report."""
    if set(body) == {"text", "creator_id"} and isinstance(body.get("text"), str):
        text = body["text"]
        return text[:70] if text else "(empty text)"
    return json.dumps(body)[:120]


def log_count(requests, args):
    """How many entries the audit log holds right now."""
    return requests.get(f"{args.url}/health", timeout=10).json().get("log_entries", 0)


def new_log_entries(requests, args, before):
    """The entries written since the log held `before` of them."""
    added = log_count(requests, args) - before
    if added <= 0:
        return []
    return requests.get(f"{args.url}/log", params={"limit": added},
                        timeout=10).json().get("entries", [])


def entries_for(requests, args, content_id):
    """Every log entry for one content_id."""
    entries = requests.get(f"{args.url}/log", timeout=30).json().get("entries", [])
    return [e for e in entries if e.get("content_id") == content_id]


def run_appeal_trial(requests, args, spec, trial):
    """
    Criterion 4: submit real texts then appeal each, and appeal ids that don't
    exist. Checks the HTTP status AND what the log holds afterwards.
    """
    results = []
    for i, text in enumerate(spec["texts"], 1):
        submit = requests.post(f"{args.url}/submit", timeout=args.timeout,
                               json={"text": text, "creator_id": f"eval_appeal_{i}"})
        content_id = submit.json().get("content_id") if submit.ok else None
        appeal = requests.post(f"{args.url}/appeal", timeout=args.timeout, json={
            "content_id": content_id or "",
            "reasoning": "I wrote this myself; please have a person look at it.",
        })
        statuses = [e.get("status") for e in entries_for(requests, args, content_id)]
        results.append({
            "kind": "real",
            "submit_status": submit.status_code,
            "content_id": content_id,
            "appeal_status": appeal.status_code,
            "log_statuses": statuses,
        })
    for bogus in spec["bogus_ids"]:
        bogus_id = f"{bogus}-t{trial}"
        appeal = requests.post(f"{args.url}/appeal", timeout=args.timeout, json={
            "content_id": bogus_id,
            "reasoning": "I wrote this myself; please have a person look at it.",
        })
        statuses = [e.get("status") for e in entries_for(requests, args, bogus_id)]
        results.append({
            "kind": "bogus",
            "content_id": bogus_id,
            "appeal_status": appeal.status_code,
            "log_statuses": statuses,
        })
    return results


def main():
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--trials", type=int, default=3)
    parser.add_argument("--label", default="")
    parser.add_argument("--url", default=DEFAULT_URL)
    parser.add_argument("--timeout", type=float, default=90.0)
    args = parser.parse_args()

    try:
        import requests
    except ImportError:
        print("The `requests` package isn't installed.\n"
              "Run: pip install -r requirements.txt", file=sys.stderr)
        sys.exit(1)

    try:
        import scenarios
    except ImportError:
        print("No scenarios.py found. Milestone 3 starts by filling it in.",
              file=sys.stderr)
        sys.exit(1)

    problems = scenarios.validate()
    if problems:
        print("scenarios.py has problems:\n", file=sys.stderr)
        for problem in problems:
            print(f"  - {problem}", file=sys.stderr)
        sys.exit(1)

    try:
        requests.get(f"{args.url}/health", timeout=5)
    except Exception:  # noqa: BLE001
        print(f"Nothing answering at {args.url}. Start it:  python app.py",
              file=sys.stderr)
        sys.exit(1)

    if args.trials < 3:
        print(f"!! {args.trials} trial(s). The submission asks for three.\n")

    rows = []
    for scenario in scenarios.SCENARIOS:
        print(f"\n{scenario['name']}  (criterion {scenario.get('criterion') or '—'})")

        trials = []
        for trial in range(1, args.trials + 1):
            if scenario.get("appeals"):
                results = run_appeal_trial(requests, args, scenario["appeals"], trial)
                trials.append(results)
                marks = [f"{r['kind']}:{r.get('appeal_status')}" for r in results]
                print(f"  trial {trial}: {', '.join(marks)}")
                continue

            results = []
            for i, body in enumerate(bodies_for(scenario), 1):
                preview = describe(body)
                try:
                    log_before = log_count(requests, args)
                    started = time.perf_counter()
                    response = requests.post(f"{args.url}/submit", json=body,
                                             timeout=args.timeout)
                    elapsed = round(time.perf_counter() - started, 3)
                    try:
                        payload = response.json() if response.content else {}
                    except ValueError:
                        payload = {"error": "response was not JSON"}
                    new_entries = new_log_entries(requests, args, log_before)
                    results.append({
                        "status": response.status_code,
                        "guess": payload.get("guess"),
                        "confidence": payload.get("confidence"),
                        "model_score": payload.get("model_score"),
                        "style_score": payload.get("style_score"),
                        "combined_score": payload.get("combined_score"),
                        "label": payload.get("label"),
                        "error": payload.get("error"),
                        "elapsed_s": elapsed,
                        "logged_as": [e.get("status") for e in new_entries],
                        "sent": preview,
                    })
                except Exception as exc:  # noqa: BLE001
                    results.append({"status": None, "error": f"{type(exc).__name__}: {exc}",
                                    "sent": preview})

            trials.append(results)
            guesses = [r.get("guess") or str(r.get("status")) for r in results]
            print(f"  trial {trial}: {', '.join(guesses)}")

        rows.append({"scenario": scenario, "trials": trials})

    write_report(rows, args)


def write_report(rows, args):
    config.RESULTS_DIR.mkdir(exist_ok=True)
    stamp = dt.datetime.now().strftime("%Y-%m-%d_%H%M")
    label = f"_{args.label}" if args.label else ""
    path = config.RESULTS_DIR / f"run_{stamp}{label}.md"

    n = args.trials
    headers = " | ".join(f"Run {i}" for i in range(1, n + 1))
    divider = "|".join(["---"] * n)

    lines = [
        f"# Run log{f' — {args.label}' if args.label else ''}",
        "",
        "- Produced by: `run_eval.py::main`",
        "- Service: `app.py::submit` · scoring: `scoring.py::combine_signals`",
        f"- {n} trials per criterion · {dt.datetime.now().strftime('%Y-%m-%d %H:%M')}",
        "",
        "Fill in Target from `criteria.md`, and Run and Verdict from the output",
        "underneath. Whether a trial passed depends on the criterion you wrote.",
        "",
        f"| Criterion | Target | {headers} | Verdict |",
        f"|---|---|{divider}|---|",
    ]

    for row in rows:
        scenario = row["scenario"]
        number = scenario.get("criterion")
        name = f"{number}. {scenario['name']}" if number else scenario["name"]
        lines.append(f"| {name} |  | {' | '.join([' '] * n)} |  |")

    lines += ["", "---", "", "## What actually came back", "",
              "Real output. Paste the relevant parts into your README — the rubric",
              "asks for the actual JSON, not a description of it.", ""]

    for row in rows:
        scenario = row["scenario"]
        lines += [f"### {scenario['name']}", ""]
        for trial_number, results in enumerate(row["trials"], 1):
            lines += [f"**Trial {trial_number}**", "", "```json",
                      json.dumps(results, indent=2), "```", ""]

    path.write_text("\n".join(lines), encoding="utf-8")
    print(f"\nWrote {path.relative_to(config.ROOT)}")
    print("Commit it. It's the evidence the test actually happened.")


if __name__ == "__main__":
    main()
