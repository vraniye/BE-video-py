import subprocess
import os
import ffmpeg_streaming
import uuid
import psycopg

from flask import Flask, request, redirect, render_template
from ffmpeg_streaming import Formats
from sql_queires import *



app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = './source/'
app.config['ALLOWED_EXTENSIONS'] = {'mp4'}
url = os.getenv('DATABASE_URL')
#url = 'postgresql://postgres:postgres/localhost:5433/postgres'

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

@app.get('/')
def index():
    return {
        'msg': 'Homepage'
    }, 200

@app.route('/api/upload', methods=['POST'])
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
        return 'File successfully uploaded'
    else:
        return 'Invalid file type'

@app.route('/api/process/<filename>', methods=['POST'])
def video_to_chank(filename):
    path = rf'./source\{filename}'
    video = ffmpeg_streaming.input(path)
    image_path = path.replace('.mp4', '')
    file_name = os.path.basename(path.replace('.mp4', ''))
    myuuid = uuid.uuid4()

    subprocess.call(["ffmpeg", "-i", path, "-ss", "00:00:00.000", "-vframes", '1', image_path + ".jpg", "-y"],
                    stderr=subprocess.DEVNULL, stdout=subprocess.DEVNULL)
    dash = video.dash(Formats.h264())
    dash.auto_generate_representations()
    dash.output(f'./source/{myuuid}/{file_name}.mpd')
    with psycopg.connect(url) as connection:
        with connection.cursor() as cursor:
            cursor.execute(CREATE_VIDEO_TABLE)
            cursor.execute(INSERT_VIDEO, (file_name, myuuid,  image_path + ".jpg", f'./source/{myuuid}/{file_name}.mpd'))
    return 'File successfully processed'

if __name__ == '__main__':
    if not os.path.exists(app.config['UPLOAD_FOLDER']):
        os.makedirs(app.config['UPLOAD_FOLDER'])
    app.run(host='127.0.0.1', port='8080', debug=True, threaded=True)