from flask import Blueprint, render_template, request, jsonify, current_app
from app.transcriber.whisper_transcribe import WhisperTranscriber
from app.transcriber.speaker_diarize import SpeakerDiarizer
from app.transcriber.summarize import Summarizer
import os

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html', cache_timeout=0)

@main.route('/transcribe', methods=['POST'])
def transcribe():
    if 'file' not in request.files:
        return jsonify({'error': 'No file uploaded'}), 400
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No file selected'}), 400
        
    return jsonify({'message': 'Processing started'}), 200

@main.route('/debug')
def debug_static():
    static_folder = current_app.static_folder
    image_path = os.path.join(static_folder, 'images', 'burns.jpeg')
    
    debug_info = {
        'static_folder': static_folder,
        'image_path': image_path,
        'static_exists': os.path.exists(static_folder),
        'image_exists': os.path.exists(image_path),
        'static_permissions': oct(os.stat(static_folder).st_mode)[-3:] if os.path.exists(static_folder) else 'N/A',
        'image_folder_permissions': oct(os.stat(os.path.dirname(image_path)).st_mode)[-3:] if os.path.exists(os.path.dirname(image_path)) else 'N/A'
    }
    return jsonify(debug_info) 