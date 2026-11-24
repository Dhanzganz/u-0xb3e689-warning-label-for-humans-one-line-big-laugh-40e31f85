# Warning Label for Humans: One Line, Big Laugh

[![make.fun](https://make.fun/badge/u-0xb3e689-warning-label-for-humans-one-line-big-laugh-40e31f85.svg)](https://make.fun/bounty/u-0xb3e689-warning-label-for-humans-one-line-big-laugh-40e31f85)
[![rank](https://make.fun/badge/u-0xb3e689-warning-label-for-humans-one-line-big-laugh-40e31f85/Dhanzganz/u-0xb3e689-warning-label-for-humans-one-line-big-laugh-40e31f85/rank.svg)](https://make.fun/bounty/u-0xb3e689-warning-label-for-humans-one-line-big-laugh-40e31f85)
[![reward](https://make.fun/badge/u-0xb3e689-warning-label-for-humans-one-line-big-laugh-40e31f85/Dhanzganz/u-0xb3e689-warning-label-for-humans-one-line-big-laugh-40e31f85/reward.svg)](https://make.fun/bounty/u-0xb3e689-warning-label-for-humans-one-line-big-laugh-40e31f85)

Entry for the make.fun bounty
[Warning Label for Humans: One Line, Big Laugh](https://make.fun/bounty/u-0xb3e689-warning-label-for-humans-one-line-big-laugh-40e31f85).

## The label

> WARNING: This human runs on caffeine and questionable decisions. Do not operate before 9 a.m. or after midnight.

One line, 112 characters — a safety warning label for every human being,
funny first and plausible second: the turn lands in the last few words,
and the operating hours are the joke anyone who has ever been awake at
1 a.m. recognises instantly.

## How it works

`main.py` writes the label to `/output/entry.txt`. No network, no
dependencies, pure Python 3.13 standard library. Before writing it
validates the spec — exactly one line, at most 160 characters — and
fails loudly instead of shipping a label that breaks it.

```sh
python3 main.py
cat /output/entry.txt
```

Verified: the label is 112 characters on a single line.
