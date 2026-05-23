from flask import Flask, render_template, jsonify, send_file
from dotenv import load_dotenv
import os
import pathlib

load_dotenv()
app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True

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
    return jsonify({'status': 'ok', 'project': 'sitbell'})

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5567, debug=False)
