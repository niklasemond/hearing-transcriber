print("Testing all required imports...")

try:
    print("\n1. Testing Flask...")
    from flask import Flask
    print("✓ Flask imported successfully!")
except Exception as e:
    print("✗ Flask import failed:", str(e))

try:
    print("\n2. Testing Pyannote...")
    from pyannote.audio import Pipeline
    print("✓ Pyannote imported successfully!")
except Exception as e:
    print("✗ Pyannote import failed:", str(e))

try:
    print("\n3. Testing OpenAI...")
    from openai import OpenAI
    print("✓ OpenAI imported successfully!")
except Exception as e:
    print("✗ OpenAI import failed:", str(e))

try:
    print("\n4. Testing Whisper...")
    import whisper
    print("✓ Whisper imported successfully!")
except Exception as e:
    print("✗ Whisper import failed:", str(e))

print("\nImport test complete!")