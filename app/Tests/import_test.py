print("Starting import test...")

try:
    print("1. Trying to import Pipeline...")
    from pyannote.audio import Pipeline
    print("✓ Pipeline imported successfully!")
except Exception as e:
    print("✗ Failed to import Pipeline:", str(e))

print("\nTest complete!")