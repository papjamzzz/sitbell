# Melt — Re-Entry File
*Claude: read this before touching anything.*

---

## What This Is
**Melt** — dissolution meditation timer. Hypercolor neon ice video, floating glass UI, auto-hide controls, scroll drum time picker. Built for people who resonate with impermanence and dissolution as a practice.

Companion app **Time** will be a cleaner, more functional version (Tim's feature set) — separate build.

## Re-Entry Phrase
> "Re-entry: melt"

## Current Status
🚀 Ready for Railway deployment → melt.creativekonsoles.com

## Stack
- Python + Flask (gunicorn in prod)
- Local dev: port 5567, host 127.0.0.1
- Prod: Railway, PORT env var, host 0.0.0.0
- Space Grotesk + JetBrains Mono fonts
- Fullscreen ice video background (static/melt.mp4)
- Hypercolor CSS: hue-rotate(195deg) saturate(4) — electric cyan/magenta

## File Structure
```
sitbell/           ← folder name stays sitbell locally
├── app.py
├── templates/index.html
├── static/
│   ├── melt.mp4       ← fullscreen ice video
│   ├── manifest.json
│   ├── sw.js
│   └── icons/
├── data/
├── requirements.txt   ← includes gunicorn
├── Procfile           ← Railway start command
├── railway.toml       ← Railway config
├── Makefile
├── launch.command
├── .env
└── .env.example
```

## How to Run (Local)
```bash
cd ~/sitbell && make run
```

## How to Deploy
1. Connect `papjamzzz/sitbell` repo to Railway
2. Add env var: `RAILWAY_ENVIRONMENT=production`
3. Point custom domain: `melt.creativekonsoles.com`
4. Optional: set `SOUNDS_DIR` env var to a mounted volume path for bell sounds

## GitHub
- Repo: papjamzzz/sitbell
- Push: `make m="your message" push`

## What's Done
- [x] Full PWA meditation timer — timer ring, duration presets, intervals, bell sounds
- [x] Web Audio API bell scheduling (precise, survives tab background)
- [x] Synthesized fallback bell (FM synthesis)
- [x] Sound files served from ~/Desktop/timers change (local) or SOUNDS_DIR env var (prod)
- [x] Service worker + PWA manifest
- [x] Settings panel: start/end/interval bells, strike count, vibrate, wake lock
- [x] Saved presets (localStorage), long-press to delete
- [x] Wake Lock API + Notifications API
- [x] Fullscreen hypercolor ice video (melt.mp4)
- [x] Neon glitch overlay: grain, scanlines, chromatic aberration, HUD brackets, scan sweep
- [x] UI redesign: Space Grotesk + JetBrains Mono, glass panels, neon cyan/magenta palette
- [x] Auto-hide floating UI (3.2s inactivity → only ice + timer visible)
- [x] Scroll drum time picker (5m → 4h), default 1h (Vipassana)
- [x] Timer format handles h:mm:ss for sessions ≥ 1h
- [x] Railway-ready: PORT env var, gunicorn, Procfile, railway.toml, SOUNDS_DIR configurable
- [x] Renamed SitBell → Melt

## What's Next
- [ ] Deploy to Railway + set melt.creativekonsoles.com
- [ ] Drop real bell sounds into ~/Desktop/timers change (export from Ableton as WAV 24-bit 44.1kHz)
- [ ] iOS home screen icons (192×192 + 512×512 PNG in static/icons/)
- [ ] Three separate bell pickers: start / interval / end (independent sound selection)
- [ ] Begin "Time" app (separate project, Tim's feature set)

## Key Technical Decisions
- localhost only in dev (127.0.0.1), 0.0.0.0 in prod (RAILWAY_ENVIRONMENT check)
- Sound scheduling via AudioContext.currentTime — stays accurate when backgrounded
- Sounds served live from SOUNDS_DIR — no restart needed
- Auto-hide: body.idle class, CSS opacity transition, all .floatui elements
- Drum picker: 15 values 5m–4h, wheel + touch drag, syncs with setDuration()

## Last Session
Renamed SitBell → Melt. Full UI redesign with fullscreen ice video, hypercolor glass
panels, Space Grotesk + JetBrains Mono. Auto-hide floating UI (3.2s idle). Scroll drum
time picker defaults to 1h (Vipassana). Railway deployment files added. Ready to deploy
to melt.creativekonsoles.com. Companion app "Time" (functional, Tim's features) next.

---
*Last updated: 2026-05-24*
