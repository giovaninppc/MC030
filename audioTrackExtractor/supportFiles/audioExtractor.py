import sys
from moviepy.editor import *

class VideoConverter():
    def __init__(self, filePath):
        self.filePath = filePath
        self.clip = VideoFileClip(filePath)

    def getAudioFromVideo(self, audioPath):
        audio = self.clip.audio
        audio.write_audiofile(audioPath)

    def getVideoDuration(self):
        return (self.clip.duration)
