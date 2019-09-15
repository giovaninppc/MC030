from video import *
from image import *
from downloader import *

# Processing video
# processor = VideoProcessor()
# processor.detectObjectsFromVideo('assets/traffic-mini.mp4')

# Processing Images
# img_processor = ImageProcessor()
# img_processor.detectObjectsFromImage('assets/img01.png')

pytube = PytubeDownloader()
pytube.downloadVideo('https://www.youtube.com/watch?v=gAeaR3Ggmok')
