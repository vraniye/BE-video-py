import glob
import ffmpeg_streaming
import subprocess
from ffmpeg_streaming import Formats

for path in glob.glob('../videoFull/*.mp4'):

	video = ffmpeg_streaming.input(path)
	print(video)
	name = path.replace('.mp4', '')


	subprocess.call(["ffmpeg", "-i", path, "-ss", "00:00:00.000", "-vframes", '1', name + ".jpg", "-y"], stderr=subprocess.DEVNULL, stdout=subprocess.DEVNULL)
	dash = video.dash(Formats.h264())
	dash.auto_generate_representations()
	dash.output(f'dash/{name}.mpd')
