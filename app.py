from flask import Flask, request, redirect, render_template
from service.ffmpegService import videoToChank
import os
import threading


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = './source/'  # Directory where uploaded files will be stored
app.config['ALLOWED_EXTENSIONS'] = {'mp4'}  # Allowed file extensions

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return redirect(request.url)
    file = request.files['file']
    if file.filename == '':
        return redirect(request.url)
    if file and allowed_file(file.filename):
        filename = file.filename
        path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(path)
        threading.Thread(target=videoToChank, args=(filename,)).start()
        return 'File successfully uploaded'
    else:
        return 'Invalid file type'


if __name__ == '__main__':
    if not os.path.exists(app.config['UPLOAD_FOLDER']):
        os.makedirs(app.config['UPLOAD_FOLDER'])
    app.run(host='127.0.0.1', port='8080', debug=True, threaded=True)