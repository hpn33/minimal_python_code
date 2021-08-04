from ffmpy import FFmpeg

p = 'C:/ffmpeg/ffmpeg.exe'
f = 'e:/users/download/music/new folder (3)/60572-40.mp3'

ff = FFmpeg(
	executable=p,
	inputs={f: None},
	outputs={'60572-40.o.mp3': '-c copy -ss 00:32:15 -t 00:00:30'}
)

print(ff.cmd)

ff.run()
