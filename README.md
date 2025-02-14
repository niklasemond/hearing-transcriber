# Congressional Hearing Transcriber

A Flask-based web application that automatically transcribes congressional hearing audio files, identifies speakers, and generates analytical summaries. Built for researchers, journalists, and policy analysts working with congressional hearing recordings.

## Features
- High-accuracy speech-to-text transcription using OpenAI Whisper
- Automatic speaker identification and separation using Pyannote (not yet attributing the actual identity of the speaker)
- Web interface for easy file uploads (not yet tested) 
- Multiple output formats (JSON, TXT, SRT)
- Real-time processing status updates
- Secure file handling and storage (at your own risk) 

## Installation

1. Clone the repository:
   git clone https://github.com/YOUR-USERNAME/hearing-transcriber.git
   cd hearing-transcriber

2. Create and activate a virtual environment:
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate

3. Install required packages:
   pip install -r requirements.txt

4. Create a .env file with required tokens:
   SECRET_KEY=your_flask_secret_key
          - This is a random string you generate for Flask security
          - You can generate one in Python using:
              _import secrets
              print(secrets.token_hex(16)_
          - Copy the output and use it as your SECRET_KEY

   HF_TOKEN=your_huggingface_token
      - Create account at Hugging Face (https://huggingface.co/)
      - Go to Settings → Access Tokens 
      - Click "New token"
      - Give it a name (e.g., "hearing-transcriber")
      - Select "read" access
      - Accept the model terms:
      - Visit Speaker Diarization model
      - Click "Accept terms" button
      - Visit Segmentation model
      - Click "Accept terms" button

## Prerequisites

1. System Requirements:
   - Python 3.10+
   - ffmpeg
   - 8GB+ RAM recommended

2. API Access:
   - Hugging Face account (https://huggingface.co)
   - Accept terms for pyannote/speaker-diarization
   - Accept terms for pyannote/segmentation

## Usage

1. Start the Flask server:
   python run.py

2. Open your browser and navigate to:
   http://localhost:5000

3. Upload an audio file (MP3 or WAV format)
   - Maximum file size: 16MB
   - Supported formats: MP3, WAV

4. Wait for processing to complete
   - Progress will be shown in real-time
   - Results will be available for download

## Output Files

- transcript.json: Full transcript with speaker labels and timestamps
- transcript.txt: Human-readable transcript with summary
- transcript.srt: Subtitle format with speaker identification

## Project Structure

/app
  /static        - Static assets and uploaded images
  /storage       - Temporary file storage
  /templates     - HTML templates
  /transcriber   - Core transcription logic
  /config        - Application configuration

## Security Notes

- All uploaded files are securely handled
- Temporary files are automatically cleaned
- File extensions are strictly validated
- Maximum file size is enforced

## License

MIT License - See LICENSE file for details