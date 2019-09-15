# Using YOLOv3 to make the computer vision processing
# Neural network

from imageai.Detection import VideoObjectDetection
import os

# Parameters
yolo_network_path = 'neural/yolo.h5'
frames_per_second = 10

class VideoProcessor():
    def __init__(self):
        self.execution_path = os.getcwd()
        self.configureVideoDetector()

    def configureVideoDetector(self):
        self.detector = VideoObjectDetection()
        self.detector.setModelTypeAsYOLOv3()
        self.detector.setModelPath( os.path.join(self.execution_path , yolo_network_path))
        self.detector.loadModel()

    def detectObjectsFromVideo(self, filePath: str):
        video_file_path = filePath
        outPath = 'out/' + video_file_path.replace('/', '-')

        video_path = self.detector.detectObjectsFromVideo(input_file_path=os.path.join( self.execution_path, video_file_path),
                                        output_file_path = os.path.join(self.execution_path, outPath),
                                        frames_per_second = frames_per_second,
                                        log_progress = True)

        # Check for the information we can have processing the video
        print(video_path)
