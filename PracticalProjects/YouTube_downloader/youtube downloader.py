import pytube

link = "https://www.youtube.com/watch?v=lu8m5FA2nL8&ab_channel=TheKiffness"
yt = pytube.YouTube(link)
yt.streams.get_audio_only().download()


print("Downloaded:", link)
