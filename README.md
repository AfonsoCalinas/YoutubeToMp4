# Youtube Downloader To MP4

![OS](https://img.shields.io/badge/Windows-%20-9cf) [![Python3.11.3](https://img.shields.io/badge/Python3.11.3-%20-important)](https://www.python.org/ftp/python/3.11.3/python-3.11.3-amd64.exe) ![Pytube](https://img.shields.io/badge/Pytube%2015.0.0-%20-success)

A program that uses the python libraries <b>Pytube</b> and <b>FFMPEG</b> to downloads videos from youtube at it's best quality of audio/video possible.


# Installation 💾

I left a .txt file in the project so you can just do the following in your console (once your in the project's directory):
```
pip install -r requirements.txt
```

And I'll leave a link to [PIP](https://pypi.org/project/pip/) just in case you don't have it installed, it's really useful!

Since we're only installing FFMPEG for a Python Library, we need to also install FFMPEG itself!

I will leave a really intuitive guide [here](https://www.geeksforgeeks.org/how-to-install-ffmpeg-on-windows/) on how to install it :)


# How to use 🔍

It's pretty simple! To start the program:
```
python main.py
```

Insert your desired directory, per example:
```
A:\Users\Heisenberg\Desktop\
```

After that, the program will ask you for the youtube link, and here's an example:
```
https://www.youtube.com/watch?v=xvFZjo5PgG0&ab_channel=Duran
```

After this FFMPEG will fuse both the audio and video streams and the result is your desired video!


# Special Thanks 💖

[RainyPT](https://github.com/RainyPT) and [Ramos](https://github.com/NoPalm0il)
