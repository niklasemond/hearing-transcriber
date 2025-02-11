import os

def check_structure():
    required_dirs = [
        'app/static/images',
        'app/storage/uploads'
    ]
    
    for dir_path in required_dirs:
        exists = os.path.exists(dir_path)
        gitkeep = os.path.exists(os.path.join(dir_path, '.gitkeep'))
        print(f"\nChecking {dir_path}:")
        print(f"Directory exists: {exists}")
        print(f".gitkeep exists: {gitkeep}")

if __name__ == "__main__":
    check_structure() 