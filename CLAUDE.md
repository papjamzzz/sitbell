# sitbell — Re-Entry File
*Claude: read this before touching anything.*

---

## What This Is
Meditation timer with high-quality bells

## Re-Entry Phrase
> "Re-entry: sitbell"

## Current Status
🔨 Just created — ready to build

## Stack
- Python + Flask, port 5567, host 127.0.0.1
- Dark theme, Inter font, CSS variables
- Logo at /static/logo.png

## File Structure
```
sitbell/
├── app.py
├── templates/index.html
├── static/
├── data/
├── requirements.txt
├── Makefile
├── launch.command
├── .env
└── .env.example
```

## How to Run
```bash
cd ~/sitbell && make run
```

## GitHub
- Repo: papjamzzz/sitbell
- Push: `make m="your message" push`

## What's Done
- [x] Project scaffold created

## What's Next
- [ ] Define core functionality
- [ ] Add logo to static/
- [ ] Wire up first route/feature

## Key Technical Decisions
- localhost only (host=127.0.0.1)

---
*Last updated: 2026-05-23*
