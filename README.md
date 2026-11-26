# Rejected Olympic Sports

[![Competition](https://make.fun/badge/u-motasimfuad-rejected-olympic-sports-9d83e7da.svg)](https://make.fun/c/u-motasimfuad-rejected-olympic-sports-9d83e7da)
[![Rank](https://make.fun/badge/u-motasimfuad-rejected-olympic-sports-9d83e7da/arsalive-dot/rejected-olympic-sports/rank.svg)](https://make.fun/c/u-motasimfuad-rejected-olympic-sports-9d83e7da)
[![Reward](https://make.fun/badge/u-motasimfuad-rejected-olympic-sports-9d83e7da/arsalive-dot/rejected-olympic-sports/reward.svg)](https://make.fun/c/u-motasimfuad-rejected-olympic-sports-9d83e7da)

One funny single-line sport the Olympics turned down, for the
[Rejected Olympic Sports](https://make.fun/c/u-motasimfuad-rejected-olympic-sports-9d83e7da)
competition on [make.fun](https://make.fun).

## The entry

> Synchronised sighing: four athletes exhale in perfect unison while judges score depth, timing and visible disappointment.

## How it works

`main.py` (Python 3, standard library only) writes the line to
`/output/entry.txt` deterministically — via a temp file plus
`os.replace` and `chmod 644` — and self-checks the gate before writing:
UTF-8 text, a single line, 1–200 characters, not only white space.

Run it locally:

```sh
python3 main.py
cat /output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
