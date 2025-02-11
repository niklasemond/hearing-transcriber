from app import create_app
import os
import sys

print("=== Starting Flask Application ===")
print(f"Current directory: {os.getcwd()}")
print(f"Python path: {sys.path}")

try:
    print("\n1. Creating Flask app...")
    app = create_app()
    print("✓ Flask app created")

    if __name__ == "__main__":
        print("\n=== Starting server ===")
        app.run(debug=True)

except Exception as e:
    print(f"\n✗ Error: {str(e)}")
    print(f"Error type: {type(e)}")