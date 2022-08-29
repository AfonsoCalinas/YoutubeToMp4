import pytube
import ffmpeg
import os

SAVE_PATH = "C:\\Users\\<user>\\Desktop\\YoutubeToMp4\\resources"

link = input("> ")
yt = pytube.YouTube(link)

resolution = yt.streams.filter(progressive=False, file_extension='mp4', type='video').order_by('resolution')
audio = yt.streams.filter(progressive=False, file_extension='mp4', type='audio').order_by('abr')

for i in reversed(resolution):
    if i == (yt.streams.get_by_itag(299)):
        streamVideo = i
        break
    elif i == (yt.streams.get_by_itag(298)):
        streamVideo = i
        break
    elif i == (yt.streams.get_by_itag(135)):
        streamVideo = i
        break
    elif i == (yt.streams.get_by_itag(134)):
        streamVideo = i
        break

streamAudio = audio.last()

streamVideo.download(output_path=SAVE_PATH, filename='video.mp4')
streamAudio.download(output_path=SAVE_PATH, filename='audio.mp3')

video_stream = ffmpeg.input('C:\\Users\\<user>\\Desktop\\YoutubeToMp4\\resources\\video.mp4')
audio_stream = ffmpeg.input('C:\\Users\\<user>\\Desktop\\YoutubeToMp4\\resources\\audio.mp3')
ffmpeg.output(audio_stream, video_stream, 'C:\\Users\\<user>\\Desktop\\YoutubeToMp4\\output\\coolvideo.mp4').run()

if os.path.isfile(SAVE_PATH + '\\video.mp4') and os.path.isfile(SAVE_PATH + '\\audio.mp3'):
    os.remove(SAVE_PATH + '\\video.mp4')
    os.remove(SAVE_PATH + '\\audio.mp3')
    print("> Resources have been deleted and your video is done rendering!\n> Check output folder and retrieve your video!")
else:
    print("> Resources don't exist!")
