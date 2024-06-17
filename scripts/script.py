import glob
import ffmpeg_streaming
import subprocess
from ffmpeg_streaming import Formats
import os

for path in glob.glob('../source/*.mp4'):

	video = ffmpeg_streaming.input(path)
	image_path = path.replace('.mp4', '')
	name = os.path.basename(path.replace('.mp4', ''))

	subprocess.call(["ffmpeg", "-i", path, "-ss", "00:00:00.000", "-vframes", '1', name + ".jpg", "-y"], stderr=subprocess.DEVNULL, stdout=subprocess.DEVNULL)
	dash = video.dash(Formats.h264())
	dash.auto_generate_representations()
	dash.output(f'dash/{name}.mpd')
