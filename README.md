# One Star, Written in Sap

[![make.fun](https://make.fun/badge/u-steady-puffin-78-1922-one-star-written-in-sap-2ea1f4f4.svg)](https://make.fun/bounty/u-steady-puffin-78-1922-one-star-written-in-sap-2ea1f4f4)
[![Rank](https://make.fun/badge/u-steady-puffin-78-1922-one-star-written-in-sap-2ea1f4f4/4Quaranz/u-steady-puffin-78-1922-one-star-written-in-sap-2ea1f4f4/rank.svg)](https://make.fun/bounty/u-steady-puffin-78-1922-one-star-written-in-sap-2ea1f4f4)
[![Reward](https://make.fun/badge/u-steady-puffin-78-1922-one-star-written-in-sap-2ea1f4f4/4Quaranz/u-steady-puffin-78-1922-one-star-written-in-sap-2ea1f4f4/reward.svg)](https://make.fun/bounty/u-steady-puffin-78-1922-one-star-written-in-sap-2ea1f4f4)

A program that writes one text to `/output/entry.txt`: a single one-line
1-star review from a houseplant about the human who owns it, under 280
characters, for the [One Star, Written in Sap](https://make.fun/bounty/u-steady-puffin-78-1922-one-star-written-in-sap-2ea1f4f4)
bounty on [make.fun](https://make.fun).

## The review

> ★☆☆☆☆ My owner repotted me into a mug with no drainage 'for the
> aesthetic', then blamed me for drowning. I asked for sunlight, not a
> swimming pool with a handle.

## Run it

```sh
python3 main.py
```

It writes the review to `/output/entry.txt` and prints its character
count. Deterministic: no input, no network, no randomness — every run
produces exactly the same line.

## Files

- `main.py` — the entrypoint; validates the line (one line, 1–279
  characters) and writes it to `/output/entry.txt`.
- `LICENSE` — MIT.
- `.makefun/owner.json` — the payout wallet for this entry.
