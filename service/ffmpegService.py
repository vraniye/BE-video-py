import ffmpeg_streaming
import subprocess
import os
from ffmpeg_streaming import Formats
import uuid

def videoToChank(filename):
    print("Start")
    print(filename)
    path = rf'../source\{filename}'
    video = ffmpeg_streaming.input(path)
    image_path = path.replace('.mp4', '')
    name = os.path.basename(path.replace('.mp4', ''))
    myuuid = uuid.uuid4()

    subprocess.call(["ffmpeg", "-i", path, "-ss", "00:00:00.000", "-vframes", '1', image_path + ".jpg", "-y"],
                    stderr=subprocess.DEVNULL, stdout=subprocess.DEVNULL)
    dash = video.dash(Formats.h264())
    dash.auto_generate_representations()
    dash.output(f'../source/{myuuid}/{name}.mpd')
    print("Finish")
    return 0
