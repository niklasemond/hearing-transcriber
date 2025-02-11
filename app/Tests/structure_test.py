import os
import importlib

def check_file(filepath):
    print(f"\nChecking {filepath}")
    print(f"File exists: {os.path.exists(filepath)}")
    if os.path.exists(filepath):
        with open(filepath, 'r') as f:
            first_line = f.readline().strip()
            print(f"First line: {first_line}")

print("=== Project Structure Test ===")

# Check main files
files_to_check = [
    'app/__init__.py',
    'app/routes.py',
    'app/transcriber/__init__.py',
    'app/transcriber/speaker_diarize.py',
    'app/transcriber/whisper_transcribe.py',
    'app/transcriber/summarize.py'
]

for file in files_to_check:
    check_file(file)

print("\n=== Module Test ===")
try:
    print("\nTrying to import app...")
    import app
    print("✓ app imported")
    
    print("\nTrying to import app.transcriber...")
    import app.transcriber
    print("✓ app.transcriber imported")
    
    print("\nTrying to import SpeakerDiarizer...")
    from app.transcriber.speaker_diarize import SpeakerDiarizer
    print("✓ SpeakerDiarizer imported")
except Exception as e:
    print(f"✗ Error: {str(e)}")

print("\n=== Test Complete ===")