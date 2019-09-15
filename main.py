from video import *
from image import *
from downloader import *
from arguments import *

def processImage(path):
    img_processor = ImageProcessor()
    img_processor.detectObjectsFromImage(path)

def processVideo(path):
    processor = VideoProcessor()
    processor.detectObjectsFromVideo(path)

def downloadVideo(path):
    pytube = PytubeDownloader()
    pytube.downloadVideo(path)

# Run arguments
configuration = setupArguments()
path = configuration.path
args = configuration.args

if args.image:
    processImage(path)

if args.video:
    processVideo(path)

elif args.youtube:
    downloadVideo(path)
    processVideo('temp.mp4')
