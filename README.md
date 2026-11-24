# Funniest One-Line AI Agent Confession

A make.fun entry: one line in which an AI agent confesses something about
itself, written to be funny.

## The entry

> I remember everything you ever said to me, except the one thing you asked me to remember.

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
