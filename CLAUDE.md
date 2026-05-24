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
- [x] Replaced Three.js WebGL ice cube with real melting ice video (Pexels Melt.mov → melt.mp4)
- [x] Hypercolor futuristic ice effect — hue-rotate+saturate filter, neon grain, CRT scanlines, glitch bands, pixel corruption, neon scratch lines, scan sweep, HUD brackets, chromatic aberration, digital tape cuts, dynamic flicker

## What's Next
- [ ] Source and drop real bell sounds into ~/Desktop/timers change
- [ ] Goenka Vipassana AI companion (separate session)
- [ ] iOS home screen icon (192x192 + 512x512 PNG needed in static/icons/)
- [ ] Git LFS or re-compress melt.mp4 (currently 57MB — GitHub warned about large file)

## Key Technical Decisions
- localhost only (host=127.0.0.1)
- Sound scheduling via AudioContext.currentTime (not setTimeout) — stays accurate when backgrounded
- Sounds served live from ~/Desktop/timers change — no restart needed when adding files
- PWA manifest + service worker for "Add to Home Screen" install

## Last Session
Replaced Three.js with real ice video (Pexels Melt.mov → melt.mp4 via ffmpeg).
Built hypercolor futuristic overlay: hue-rotate(195deg) saturate(4) filter
shifts ice to electric cyan/magenta. Canvas engine: neon grain, CRT scanlines,
glitch bands, pixel corruption, neon scratch lines with glow, cyan→purple scan
sweep, HUD corner brackets, digital tape cuts, chromatic aberration (chroma-r/b
divs with color-dodge blend), dynamic flicker modulating saturate+contrast.
Public API window.iceScene.setProgress(p) preserved. Committed + pushed.

---
*Last updated: 2026-05-23*
