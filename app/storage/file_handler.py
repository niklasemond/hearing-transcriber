import os
from werkzeug.utils import secure_filename

class FileHandler:
    def __init__(self, upload_folder='uploads'):
        self.upload_folder = upload_folder
        os.makedirs(upload_folder, exist_ok=True)
    
    def save_file(self, file):
        """Saves uploaded file and returns the path"""
        filename = secure_filename(file.filename)
        path = os.path.join(self.upload_folder, filename)
        file.save(path)
        return path
    
    def get_file_path(self, filename):
        """Returns full path for a filename"""
        return os.path.join(self.upload_folder, filename)