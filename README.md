# Remote video processing
##### with Pytube and YOLOv3

### Setup the environment

- Download and install pytube
`pip3 install pytube`

- [Download YOLOv3](https://github.com/OlafenwaMoses/ImageAI/releases/download/1.0/yolo.h5) into `neural/` folder
> The neural network file is too big for github files, there is a limit for 100Mb per file

### Run the program
`python3 main.py <filepath / url> <flag>`

- `-im` process image with local file
  - Ex: `python3 assets/image.png -im`
- `-vi` process video with local file
  - Ex: `python3 assets/example.mp4 -vi`
- `-yt` download YouTube video as mp4 and process it
   -Ex: `python3 https://www.youtube.com/watch?v=gAeaR3Ggmok -yt`
