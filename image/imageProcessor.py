from imageai.Detection import ObjectDetection
import os

# Parameters
yolo_network_path = 'neural/yolo.h5'
frames_per_second = 10

class ImageProcessor():
    def __init__(self):
        self.execution_path = os.getcwd()
        self.configureVideoDetector()

    def configureVideoDetector(self):
        self.detector = VideoObjectDetection()
        self.detector.setModelTypeAsYOLOv3()
        self.detector.setModelPath( os.path.join(self.execution_path , yolo_network_path))
        self.detector.loadModel()

    def detectObjectsFromImage(self, filePath: str):
        imagePath = filePath
        outPath = 'out/' + imagePath.replace('/', '-')

        processedImage = self.detector.detectObjectsFromImage(input_image = os.path.join( self.execution_path, imagePath),
                                        output_image_path = os.path.join(self.execution_path, outPath))

        # Check for the information we can have processing the video
        print(processedImage)
        print(type(processedImage))
