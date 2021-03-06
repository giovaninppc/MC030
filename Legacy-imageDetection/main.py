from video import *
from image import *
from downloader import *
from arguments import *

def processImage(path):
    img_processor = ImageProcessor()
    img_processor.detectObjectsFromImage(path)

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


if __name__ == "__main__":
    # Run arguments
    configuration = setupArguments()
    path = configuration.path
    args = configuration.args

    if args.image:
        processImage(path)

    if args.video:
        processVideo(path, args)

    elif args.youtube:
        downloadVideo(path)
        processVideo('temp.mp4', args)
        os.remove('temp.mp4')
