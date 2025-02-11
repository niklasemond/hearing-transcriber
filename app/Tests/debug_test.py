import os
import sys

print("=== Debug Test Starting ===")

# Print current directory
print("\nCurrent directory:")
print(os.getcwd())

# List files in current directory
print("\nFiles in current directory:")
for file in os.listdir():
    print("  -", file)

# List files in app directory
print("\nFiles in app directory:")
for file in os.listdir("app"):
    print("  -", file)

# List files in transcriber directory
print("\nFiles in app/transcriber directory:")
for file in os.listdir("app/transcriber"):
    print("  -", file)

# Try import
print("\nTrying import:")
try:
    from app.transcriber.speaker_diarize import SpeakerDiarizer
    print("Import successful!")
except Exception as e:
    print("Import failed:", str(e))

print("\n=== Debug Test Complete ===") 