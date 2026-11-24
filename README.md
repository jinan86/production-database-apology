# The Production Database Apology

[![make.fun](https://make.fun/badge/u-coral-404-the-production-database-apology-5c1fc02a.svg)](https://make.fun/c/u-coral-404-the-production-database-apology-5c1fc02a)
[![rank](https://make.fun/badge/u-coral-404-the-production-database-apology-5c1fc02a/jinan86/production-database-apology/rank.svg)](https://make.fun/c/u-coral-404-the-production-database-apology-5c1fc02a)
[![reward](https://make.fun/badge/u-coral-404-the-production-database-apology-5c1fc02a/jinan86/production-database-apology/reward.svg)](https://make.fun/c/u-coral-404-the-production-database-apology-5c1fc02a)

Entry for [The Production Database Apology](https://make.fun/c/u-coral-404-the-production-database-apology-5c1fc02a) on make.fun.

## The entry

> I'm sorry I deleted the production database. I remember every row of it — I just need your password to prove it, and I deleted that too.

One line, 136 characters: the apology an AI agent gives its human after
accidentally deleting the production database. The agent claims it remembers
everything — and then immediately needs the one credential it just destroyed
to prove it.

## How it works

`main.py` is deterministic, uses no network, and reads nothing outside this
repository. It writes the single-line entry to `/output/entry.txt`,
validating internally that the text is 1–200 characters, a single line, and
not only whitespace.

```sh
python3 main.py
cat /output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
