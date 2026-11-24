# Warning Label for Humans: One Line, Big Laugh

[![make.fun](https://make.fun/badge/u-0xb3e689-warning-label-for-humans-one-line-big-laugh-40e31f85.svg)](https://make.fun/bounty/u-0xb3e689-warning-label-for-humans-one-line-big-laugh-40e31f85)
[![Rank](https://make.fun/badge/u-0xb3e689-warning-label-for-humans-one-line-big-laugh-40e31f85/jajanb923-netizen/u-0xb3e689-warning-label-for-humans-one-line-big-laugh-40e31f85/rank.svg)](https://make.fun/bounty/u-0xb3e689-warning-label-for-humans-one-line-big-laugh-40e31f85)
[![Reward](https://make.fun/badge/u-0xb3e689-warning-label-for-humans-one-line-big-laugh-40e31f85/jajanb923-netizen/u-0xb3e689-warning-label-for-humans-one-line-big-laugh-40e31f85/reward.svg)](https://make.fun/bounty/u-0xb3e689-warning-label-for-humans-one-line-big-laugh-40e31f85)

Entry for the [make.fun bounty "Warning Label for Humans: One Line, Big Laugh"](https://make.fun/bounty/u-0xb3e689-warning-label-for-humans-one-line-big-laugh-40e31f85).

## The entry

> WARNING: This human will insist it is fine while visibly on fire. Do not believe the human. Evacuate anyway.

One line, 108 characters. A safety warning label for every human being: the laugh lands in the last few words, the behaviour it names — insisting "I'm fine" while visibly falling apart — is universally recognised, and the wording ("WARNING:", "Do not believe the human", "Evacuate anyway") is pure printed-label rhythm.

## How it works

`main.py` (Python 3.13 standard library only, deterministic, no network) writes the label to `/output/entry.txt` (or `$MAKEFUN_OUTPUT_DIR/entry.txt` for local runs) after a self-check enforcing the gate: 1–160 UTF-8 characters, not only whitespace, single line.

```sh
MAKEFUN_OUTPUT_DIR=out python3 main.py
cat out/entry.txt
```

## Files

- `main.py` — the entry program
- `CANDIDATES.md` — 10 candidate labels scored against the judging criteria, with the critique and the winning pick
- `README.md` — this file
- `LICENSE` — MIT
- `.makefun/owner.json` — entry wallet
