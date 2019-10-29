from flask import Flask

UPLOAD_FOLDER = 'file-upload'
#Flask library for connecting to the main app.py
app = Flask(__name__)
app.secret_key = "secret key"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024