from imageai.Detection import ObjectDetection
import os

# Parameters
yolo_network_path = 'neural/yolo.h5'
frames_per_second = 10

class ImageProcessor():
    def __init__(self):
        self.execution_path = os.getcwd()
        self.configureImageDetector()

    def configureImageDetector(self):
        self.detector = ObjectDetection()
        self.detector.setModelTypeAsYOLOv3()
        self.detector.setModelPath( os.path.join(self.execution_path , yolo_network_path))
        self.detector.loadModel()

    def detectObjectsFromImage(self, filePath: str):
        imageFilePath = filePath
        outPath = 'out/' + imageFilePath.replace('/', '-')

        processedImage = self.detector.detectObjectsFromImage(input_image = os.path.join( self.execution_path, imageFilePath),
                                        output_image_path = os.path.join(self.execution_path, outPath),
                                        minimum_percentage_probability = 30)

        return map(lambda i: i['name'], processedImage)
