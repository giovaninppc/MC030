# Using YOLOv3 to make the computer vision processing
# Neural network

from imageai.Detection import VideoObjectDetection
import os

yolo_network_path = 'yolo.h5'
video_file_path = 'assets/traffic-mini.mp4'

out_path = 'out/' + video_file_path.replace('/', '-')

execution_path = os.getcwd()

detector = VideoObjectDetection()
detector.setModelTypeAsYOLOv3()
detector.setModelPath( os.path.join(execution_path , yolo_network_path))
detector.loadModel()

video_path = detector.detectObjectsFromVideo(input_file_path=os.path.join( execution_path, video_file_path),
                                output_file_path=os.path.join(execution_path, out_path)
                                , frames_per_second=10, log_progress=True)
print(video_path)
print(type(video_path))
