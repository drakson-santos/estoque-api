import os
import uuid
from werkzeug.utils import secure_filename

class FileController:

    def __init__(self):
        self.SERVER_NAME = "localhost:5000"
        self.UPLOAD_FOLDER = "static"

    def get_url_file(self, filename):
        return "http://"+self.SERVER_NAME+"/"+self.UPLOAD_FOLDER+"/"+filename

    def save_file(self, file):
        filename = str(uuid.uuid4())
        photo = os.path.join(self.UPLOAD_FOLDER, filename)
        file.save(photo)
        return self.get_url_file(filename)
