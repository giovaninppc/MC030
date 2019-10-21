from flask import Flask
from video import *
from image import *
from downloader import *
from arguments import *


def downloadVideo(path):
    pytube = PytubeDownloader()
    pytube.downloadVideo(path)


def processVideo(path, args):
    if args.frameByFrame:
        processVideoFrameByFrame(path)
    else:
        processEntireVideo(path)


def processEntireVideo(path):
    processor = VideoProcessor()
    processor.detectObjectsFromVideo(path)


def processVideoFrameByFrame(path):
    detectedObjects = []
    img_processor = ImageProcessor()
    frame_extractor = FrameExtractor(path)
    while frame_extractor.getNextFrame():
        objects = img_processor.detectObjectsFromImage('frame.png')
        detectedObjects += objects
    dict = {}
    for object in detectedObjects:
        previousValue = dict.get(object) or 0
        dict[object] = previousValue + 1
    print(dict)


def downloadVideo(path):
    pytube = PytubeDownloader()
    pytube.downloadVideo(path)

app = Flask(__name__)


@app.route("/<url>")
def hello():
    return "Hello World from Flask in a uWSGI Nginx Docker container with \
     Python 3.7 (from the example template)"


if __name__ == "__main__":
    # Only for debugging while developing
    app.run(host='0.0.0.0', debug=True, port=80)
