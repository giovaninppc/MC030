import sys
from moviepy.editor import *


def getAudioFromVideo(videoPath, audioPath):

    video = VideoFileClip(videoPath)
    audio = video.audio
    audio.write_audiofile(audioPath)
