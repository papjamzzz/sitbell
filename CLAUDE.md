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
- [x] Full PWA meditation timer — timer ring, duration presets, intervals, bell sounds
- [x] Web Audio API bell scheduling (precise, survives tab background)
- [x] Synthesized fallback bell (FM synthesis, works with zero sound files)
- [x] Sound files served from ~/Desktop/timers change — drop files there, they appear instantly
- [x] Service worker for offline/installable PWA
- [x] Settings panel: start/end/interval bells, strike count (1/2/3), vibrate mode, wake lock
- [x] Saved presets (localStorage), long-press to delete
- [x] Wake Lock API — screen stays on during session
- [x] Notifications API for lock screen progress

## What's Next
- [ ] Source and drop real bell sounds into ~/Desktop/timers change
- [ ] Goenka Vipassana AI companion (separate session)
- [ ] iOS home screen icon (192x512 PNG needed in static/icons/)

## Key Technical Decisions
- localhost only (host=127.0.0.1)
- Sound scheduling via AudioContext.currentTime (not setTimeout) — stays accurate when backgrounded
- Sounds served live from ~/Desktop/timers change — no restart needed when adding files
- PWA manifest + service worker for "Add to Home Screen" install

## Last Session
Shipping v1 ice cube centerpiece. View-space matcap shader — Fresnel rim,
three specular lights in view space, correct coordinate spaces. Arc:
pristine crystal outline → condensation droplets (progress 12%) → frost
builds (roughness uniform) → cracks (38-75%) → shrinks into puddle. Timer,
sounds, presets, wake lock, service worker all complete.

---
*Last updated: 2026-05-23*
