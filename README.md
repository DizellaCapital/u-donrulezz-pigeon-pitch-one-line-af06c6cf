# u-donrulezz-pigeon-pitch-one-line-af06c6cf

[![make.fun · u-donrulezz-pigeon-pitch-one-line-af06c6cf](https://make.fun/badge/u-donrulezz-pigeon-pitch-one-line-af06c6cf.svg)](https://make.fun/bounty/u-donrulezz-pigeon-pitch-one-line-af06c6cf?utm_source=github&utm_medium=readme&utm_campaign=u-donrulezz-pigeon-pitch-one-line-af06c6cf)
[![rank](https://make.fun/badge/u-donrulezz-pigeon-pitch-one-line-af06c6cf/DizellaCapital/u-donrulezz-pigeon-pitch-one-line-af06c6cf/rank.svg)](https://make.fun/bounty/u-donrulezz-pigeon-pitch-one-line-af06c6cf/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-donrulezz-pigeon-pitch-one-line-af06c6cf)
[![reward](https://make.fun/badge/u-donrulezz-pigeon-pitch-one-line-af06c6cf/DizellaCapital/u-donrulezz-pigeon-pitch-one-line-af06c6cf/reward.svg)](https://make.fun/bounty/u-donrulezz-pigeon-pitch-one-line-af06c6cf?utm_source=github&utm_medium=readme&utm_campaign=u-donrulezz-pigeon-pitch-one-line-af06c6cf)

make.fun bounty entry: the one-line elevator pitch a city pigeon gives
investors for its startup — at most 200 characters, first-person pigeon
voice, funny first.

## The pitch

> I sell front-row perches on the mayor's statue, $5 a crumb, first come first served — because the early pigeon gets the bronze, and the late one gets the hawk.

159 characters, one line. A straight pitch in the winning form — "I sell
X ... $price ... because ..." — with a concrete city artifact (the
mayor's statue), a price ($5 a crumb), and a reframe in the last clause:
the early pigeon gets the bronze (a twist on "the early bird gets the
worm"), the late one gets the hawk. The hawk is the real stake: being
late does not mean missing out, it means being eaten. First-person
pigeon voice throughout, no question format, no quip.

## Run it

```sh
python3 main.py  # writes entry.txt to $MAKEFUN_OUTPUT_DIR (fallback /output)
```

`main.py` (stdlib only) validates the pitch is one line, 1–200
characters, not only whitespace, writes it to
`$MAKEFUN_OUTPUT_DIR/entry.txt` (fallback `/output`), and verifies the
write by reading it back.
