from pytube import YouTube
import  pytube


def takedata(data):
    yt = YouTube(data)

    print(yt.title)
    print(yt.thumbnail_url)
    stream = yt.streams.get_by_itag(22)
    print("Downloading start")
    stream.download()
    print("File is downloaded")



