# https://stackoverflow.com/questions/33311153/python-extracting-and-saving-video-frames

import cv2
import os
import numpy as np

class FrameExtractor():
    def __init__(self, path):
        self.path = path
        self.count = 0
        self.vidcap = cv2.VideoCapture(self.path)

    def getNextFrame(self):
        success = True

        self.vidcap.set(cv2.CAP_PROP_POS_MSEC,(self.count * 1000))
        success, image = self.vidcap.read()

        if success == False:
            self.clearFrames()
            return False

        cv2.imwrite('frame.png', image)     # save frame as PNG file
        print('' + str(self.count) + '.sec reading a new frame: ' + str(success))
        self.count += 1

        return success

    def clearFrames(self):
        os.remove('frame.png')
