from flask import Flask, render_template, jsonify, send_file
from dotenv import load_dotenv
import os
import pathlib

load_dotenv()
app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True

# Sounds dir: env var override, else ~/Desktop/timers change (local dev)
# On Railway, drop .wav files into /sounds/ volume or set SOUNDS_DIR env var
_sounds_env = os.environ.get('SOUNDS_DIR')
if _sounds_env:
    SOUNDS_DIR = pathlib.Path(_sounds_env)
else:
    SOUNDS_DIR = pathlib.Path.home() / "Desktop" / "timers change"

AUDIO_EXTENSIONS = {'.wav', '.mp3', '.aif', '.aiff', '.flac', '.ogg', '.m4a'}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/sounds')
def list_sounds():
    sounds = []
    if SOUNDS_DIR.exists():
        for f in sorted(SOUNDS_DIR.iterdir()):
            if f.suffix.lower() in AUDIO_EXTENSIONS:
                sounds.append({'name': f.stem, 'filename': f.name})
    return jsonify(sounds)

@app.route('/sounds/<path:filename>')
def serve_sound(filename):
    filepath = SOUNDS_DIR / filename
    if filepath.exists() and filepath.suffix.lower() in AUDIO_EXTENSIONS:
        return send_file(filepath)
    return jsonify({'error': 'not found'}), 404

@app.route('/api/status')
def status():
    return jsonify({'status': 'ok', 'project': 'melt'})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5567))
    host = '0.0.0.0' if os.environ.get('RAILWAY_ENVIRONMENT') else '127.0.0.1'
    app.run(host=host, port=port, debug=False)
