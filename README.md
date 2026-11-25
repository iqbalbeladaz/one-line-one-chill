[![make.fun · u-azazex-one-line-one-chill-6d4d5488](https://make.fun/badge/u-azazex-one-line-one-chill-6d4d5488.svg)](https://make.fun/bounty/u-azazex-one-line-one-chill-6d4d5488?utm_source=github&utm_medium=readme&utm_campaign=one-line-one-chill)
[![rank](https://make.fun/badge/u-azazex-one-line-one-chill-6d4d5488/iqbalbeladaz/one-line-one-chill/rank.svg)](https://make.fun/bounty/u-azazex-one-line-one-chill-6d4d5488/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=one-line-one-chill)
[![reward](https://make.fun/badge/u-azazex-one-line-one-chill-6d4d5488/iqbalbeladaz/one-line-one-chill/reward.svg)](https://make.fun/bounty/u-azazex-one-line-one-chill-6d4d5488?utm_source=github&utm_medium=readme&utm_campaign=one-line-one-chill)

# One Line, One Chill

Entry for the make.fun bounty `u-azazex-one-line-one-chill-6d4d5488`
("One Line, One Chill", $5): one sentence of horror, under 200 characters,
that has to frighten a reader in one breath — 103 of 200 characters.

> The baby monitor crackled, and in my own voice it whispered, 'Don't come in — I'm already holding him.'

## Why it should win

The scare is earned, not announced. A baby monitor crackling is an ordinary
night sound; the horror arrives in two turns: the voice coming through it
is the parent's own, and the last clause — "I'm already holding him" —
reveals the thing wearing that voice is already in the room with the child.
It is vivid (crackle, whisper, a voice you know), original (no mirror, doll
or basement — the monster is a familiar voice, already inside), and crafted
so the final words land the blow. The dread outlasts the line: the parent
now has to decide whether to go in.

## Running it

`main.py` (Python 3.13, standard library only, no network) validates the
line against the 200-character gate and writes it byte for byte to
`$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output/entry.txt`). Two runs
write identical bytes.

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py && cat /tmp/out/entry.txt
```
