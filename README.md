# Youtube Downloader To MP4

![OS](https://img.shields.io/badge/Windows-%20-9cf) [![Python3.9](https://img.shields.io/badge/Python3.9-%20-important)](https://www.python.org/downloads/release/python-390/) ![Pytube](https://img.shields.io/badge/Pytube%2012.1.0-%20-success) ![FFMPEG](https://img.shields.io/badge/FFMPEG-%20-ff69b4)

A program that uses the python libraries <b>Pytube</b> and <b>FFMPEG</b> to downloads videos from youtube at it's best quality of audio/video possible.

Note: 1080p or less, since the <b>default video codec</b> from windows doesn't support qualities above 1080p.


# Very Important Note ⚠️

In order for Pytube Library to work, I had to make a quick fix on it's Library code.

Found this fix through the user [Peter Guan](https://stackoverflow.com/users/18861399/peter-guan?tab=profile), on a Stack Overflow Post, which I will link [here](https://stackoverflow.com/questions/71907725/pytube-exceptions-regexmatcherror-get-throttling-function-name-could-not-find).

In a few words, what you have to do:

1. Open the file cypher.py on your Pytube Library Folder, that should be around here:
```
C:\Users\<user>\AppData\Local\Programs\Python\Python39\Lib\site-packages\pytube
```
2. Now after you open cypher.py in your IDE, go to line 255, where there should be the function ```get_throttling_function_name```

3. Inside that function there's a variable called ```function_patterns``` and I had to changed it to this:
```
r'a\.[a-zA-Z]\s*&&\s*\([a-z]\s*=\s*a\.get\("n"\)\)\s*&&\s*'
r'\([a-z]\s*=\s*([a-zA-Z0-9$]+)(\[\d+\])?\([a-z]\)',
```

So you should end up with something like this:
```
function_patterns = [
        # https://github.com/ytdl-org/youtube-dl/issues/29326#issuecomment-865985377
        # https://github.com/yt-dlp/yt-dlp/commit/48416bc4a8f1d5ff07d5977659cb8ece7640dcd8
        # var Bpa = [iha];
        # ...
        # a.C && (b = a.get("n")) && (b = Bpa[0](b), a.set("n", b),
        # Bpa.length || iha("")) }};
        # In the above case, `iha` is the relevant function name
        r'a\.[a-zA-Z]\s*&&\s*\([a-z]\s*=\s*a\.get\("n"\)\)\s*&&\s*'
        r'\([a-z]\s*=\s*([a-zA-Z0-9$]+)(\[\d+\])?\([a-z]\)',
    ]
```

4. Now that that's done, check around line 311 for a variable called ```name``` (inside the ```get_throttling_function_code``` function).

5. Once you find it, just replace it with the following:
```
name = re.escape(get_throttling_function_name(js))
```

6. And your done :)


# Installation 

I left a .txt file in the project so you can just do the following in your console (once your in the project's directory):
```
pip install -r requirements.txt
```

And I'll leave a link to [PIP](https://pypi.org/project/pip/) just in case you don't have it installed, it's really usefull!


# How to use

It's pretty simple! Just go into the project's directory and do the following:
```
python main.py
```
To start the program.

Now a little arrow will pop up and all you need to do is paste the link of your youtube video!

Once you pasted it and clicked enter, the program will download both video and audio streams from the video you've chosen to the resources folder, and with the help of FFMPEG Library, it will merge them into one single cool video that you want :)

Make sure you take your cool video out of the folder, since if you run the program again, the program will ask you if you want to overwrite the cool video you had in the first place.

# Special Thanks

[RainyPT](https://github.com/RainyPT) and [Ramos](https://github.com/NoPalm0il)
