from downloader import PytubeDownloader
from video import VideoProcessor, FrameExtractor
from image import ImageProcessor


def downloadVideo(path):
    pytube = PytubeDownloader()
    pytube.downloadVideo(path)


def processVideo(path, frame_by_frame_flag):
    if frame_by_frame_flag == '1':
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
