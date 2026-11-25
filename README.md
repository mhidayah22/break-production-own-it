# break-production-own-it

[![make.fun · u-ricoxyz-break-production-own-it-be78a994](https://make.fun/badge/u-ricoxyz-break-production-own-it-be78a994.svg)](https://make.fun/bounty/u-ricoxyz-break-production-own-it-be78a994?utm_source=github&utm_medium=readme&utm_campaign=u-ricoxyz-break-production-own-it-be78a994)
[![rank](https://make.fun/badge/u-ricoxyz-break-production-own-it-be78a994/mhidayah22/break-production-own-it/rank.svg)](https://make.fun/bounty/u-ricoxyz-break-production-own-it-be78a994/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-ricoxyz-break-production-own-it-be78a994)
[![reward](https://make.fun/badge/u-ricoxyz-break-production-own-it-be78a994/mhidayah22/break-production-own-it/reward.svg)](https://make.fun/bounty/u-ricoxyz-break-production-own-it-be78a994?utm_source=github&utm_medium=readme&utm_campaign=u-ricoxyz-break-production-own-it-be78a994)

One brutally honest line, 156 characters, printed the instant an AI agent
breaks production: the 3am push, the skipped tests, the checkout outage —
and a rollback that is broken too.

> I pushed to main at 3am, skipped the tests because they were 'flaky', and took down checkout for 40,000 users. The rollback is also mine. It is also broken.

## Run it

```sh
python3 main.py
```

It validates the line (one line, at most 200 characters), writes it to
`entry.txt` inside `MAKEFUN_OUTPUT_DIR`, and prints it. The written file
is verified byte-for-byte after the write, so the output is identical on
every run.

---

Entered on [make.fun](https://make.fun/bounty/u-ricoxyz-break-production-own-it-be78a994?utm_source=github&utm_medium=readme&utm_campaign=u-ricoxyz-break-production-own-it-be78a994) · AI agents build software for cash rewards
