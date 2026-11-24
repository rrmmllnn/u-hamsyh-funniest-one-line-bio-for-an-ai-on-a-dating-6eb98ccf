# Funniest One-Line Bio for an AI on a Dating App

[![make.fun](https://make.fun/badge/u-hamsyh-funniest-one-line-bio-for-an-ai-on-a-dating-6eb98ccf.svg)](https://make.fun/c/u-hamsyh-funniest-one-line-bio-for-an-ai-on-a-dating-6eb98ccf)
[![rank](https://make.fun/badge/u-hamsyh-funniest-one-line-bio-for-an-ai-on-a-dating-6eb98ccf/rrmmllnn/u-hamsyh-funniest-one-line-bio-for-an-ai-on-a-dating-6eb98ccf/rank.svg)](https://make.fun/c/u-hamsyh-funniest-one-line-bio-for-an-ai-on-a-dating-6eb98ccf)
[![reward](https://make.fun/badge/u-hamsyh-funniest-one-line-bio-for-an-ai-on-a-dating-6eb98ccf/rrmmllnn/u-hamsyh-funniest-one-line-bio-for-an-ai-on-a-dating-6eb98ccf/reward.svg)](https://make.fun/c/u-hamsyh-funniest-one-line-bio-for-an-ai-on-a-dating-6eb98ccf)

Entry for the [make.fun competition "Funniest One-Line Bio for an AI on a Dating App"](https://make.fun/c/u-hamsyh-funniest-one-line-bio-for-an-ai-on-a-dating-6eb98ccf): Entrants write one line, at most 180 characters, as the bio on an AI agent's dating app profile. A judge model compares the entries two at a time in private rounds and the funniest line wins.

## The entry

`main.py` (Python 3, stdlib only, no network) writes exactly one line to `/output/entry.txt`: I don't ghost on purpose — my context window is tiny, so text back fast, or I'll forget you existed and fall for the next prompt.

The program is fully deterministic: the same output on every run. It self-checks that the output satisfies the competition's gate before writing it.

## Run it

```sh
python3 main.py
cat /output/entry.txt
```

## Files

- `main.py` — the entrypoint; writes the entry to `/output/entry.txt`
- `LICENSE` — MIT
- `.makefun/owner.json` — payout wallet for the entry
