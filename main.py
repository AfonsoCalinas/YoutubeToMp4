import os
from pytube import YouTube
import ffmpeg

SAVE_PATH = input("Enter the directory you wish to save your video in!\n> ")

link = input("Now insert the youtube link!\n> ")

yt = YouTube(link)

print("\nNow, checking the video's audio and video streams...")

videoStreams = yt.streams.filter(progressive=False, type="video").order_by("resolution")
video = videoStreams.last()
audioStreams = yt.streams.filter(progressive=False, type="audio", mime_type="audio/mp4").order_by("abr")
audio = audioStreams.last()

print("Downloading them...\n")

video.download(output_path= os.getcwd(), filename='video.mp4')
audio.download(output_path= os.getcwd(), filename='audio.mp3')

video_stream = ffmpeg.input(os.getcwd() + '/video.mp4')
audio_stream = ffmpeg.input(os.getcwd() + '/audio.mp3')
ffmpeg.output(audio_stream, video_stream, SAVE_PATH + "/" + yt.title + ".mp4").run()

if os.path.isfile(os.getcwd() + '/video.mp4') and os.path.isfile(os.getcwd() + '/audio.mp3'):
    os.remove(os.getcwd() + '/video.mp4')
    os.remove(os.getcwd() + '/audio.mp3')
    print("> Resources have been deleted and your video is done rendering!\n> Check output folder and retrieve your video!")
else:
    print("> Resources don't exist!")
