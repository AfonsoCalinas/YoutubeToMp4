import pytube
import ffmpeg
import os

# !!! DON'T FORGET TO CHANGE THE <user> IN LINE 7 !!!
# !!! IF YOU DO ANY CHANGES TO THE FOLDER'S NAME OR ANY OTHER NAME THAT COMPROMISES THE PROJECT'S NEEDED DIRECTORY PATHS, PLEASE DO THOSE CHANGES ON THE CODE ASWELL!!!
SAVE_PATH = "C:\\Users\\<user>\\Desktop\\YoutubeToMp4"

link = input("> ")
yt = pytube.YouTube(link)

resolution = yt.streams.filter(progressive=False, file_extension='mp4', type='video').order_by('resolution')
audio = yt.streams.filter(progressive=False, file_extension='mp4', type='audio').order_by('abr')

# Here we basically check which is the best quality possible from 1080p to 360p (in case the video is old), and get the best possible video stream
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

# Here we get the audio stream, really simple!
streamAudio = audio.last()

# We download them both with these specific names
streamVideo.download(output_path=SAVE_PATH + '\\resources', filename='video.mp4')
streamAudio.download(output_path=SAVE_PATH + '\\resources', filename='audio.mp3')

# And finnally merge them together to get the one sweet video you wished for :)
video_stream = ffmpeg.input(SAVE_PATH + '\\resources\\video.mp4')
audio_stream = ffmpeg.input(SAVE_PATH + '\\resources\\audio.mp3')
ffmpeg.output(audio_stream, video_stream, SAVE_PATH + '\\output\\coolvideo.mp4').run()

# Here we're deleting the 2 downloads we did to merge them together so that you don't have unnecessary files rolling around
if os.path.isfile(SAVE_PATH + '\\resources\\video.mp4') and os.path.isfile(SAVE_PATH + '\\resources\\audio.mp3'):
    os.remove(SAVE_PATH + '\\resources\\video.mp4')
    os.remove(SAVE_PATH + '\\resources\\audio.mp3')
    print("> Resources have been deleted and your video is done rendering!\n> Check output folder and retrieve your video!")
else:
    print("> Resources don't exist!")
