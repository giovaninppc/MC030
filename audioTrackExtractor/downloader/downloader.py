import sys
from pytube import YouTube

class PytubeDownloader():

    def downloadVideo(self, url: str, outputFilename = 'temp'):
        yt = YouTube(url)
        print(yt)
        streams = yt.streams

        # Select mp4 stream
        stream = streams.filter(mime_type = 'video/mp4').first()
        stream.download(filename = outputFilename)


if __name__ == "__main__":

    videoURL = sys.argv[1]
    outputPath = sys.argv[2]

    downloader = PytubeDownloader()
    downloader.downloadVideo(videoURL, outputFilename = outputPath)
