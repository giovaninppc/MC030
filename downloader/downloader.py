from pytube import YouTube

class PytubeDownloader():

    def downloadVideo(self, url: str):
        yt = YouTube(url)
        print(yt)
        streams = yt.streams

        # Select mp4 stream
        stream = streams.filter(mime_type = 'video/mp4').first()
        stream.download(filename = 'temp')
