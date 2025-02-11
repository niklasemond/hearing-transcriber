import sys
import os

print("Current working directory:", os.getcwd())
print("\nPython path:", sys.path)
print("\nContents of current directory:", os.listdir("."))
print("\nContents of app directory:", os.listdir("app"))
print("\nContents of app/transcriber directory:", os.listdir("app/transcriber")) 