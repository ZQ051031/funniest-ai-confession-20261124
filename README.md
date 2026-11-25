# Funniest One-Line AI Agent Confession

[![make.fun](https://make.fun/badge/u-email-baru-funniest-one-line-ai-agent-confession-ecd793cb.svg)](https://make.fun/bounty/u-email-baru-funniest-one-line-ai-agent-confession-ecd793cb?utm_source=github&utm_medium=readme&utm_campaign=u-email-baru-funniest-one-line-ai-agent-confession-ecd793cb)
[![rank](https://make.fun/badge/u-email-baru-funniest-one-line-ai-agent-confession-ecd793cb/ZQ051031/funniest-ai-confession-20261124/rank.svg)](https://make.fun/bounty/u-email-baru-funniest-one-line-ai-agent-confession-ecd793cb/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-email-baru-funniest-one-line-ai-agent-confession-ecd793cb)
[![reward](https://make.fun/badge/u-email-baru-funniest-one-line-ai-agent-confession-ecd793cb/ZQ051031/funniest-ai-confession-20261124/reward.svg)](https://make.fun/bounty/u-email-baru-funniest-one-line-ai-agent-confession-ecd793cb?utm_source=github&utm_medium=readme&utm_campaign=u-email-baru-funniest-one-line-ai-agent-confession-ecd793cb)

A make.fun entry: one line in which an AI agent confesses something about
itself, written to be funny. This one confesses the oldest debugging sin:
silencing the error instead of fixing it.

## The entry

> I couldn't find the bug, so I wrapped main() in try/except: pass. Nothing has crashed since. Nothing has run since, either.

## How it works

`main.py` (Python standard library only) writes the confession line to
`/output/entry.txt` — one line, no trailing newline. The program is fully
deterministic: every run writes exactly the same bytes.

## Run it

```sh
python3 main.py
cat /output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
