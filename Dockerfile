# FROM python:3.6.9

# FROM node:10
FROM ubuntu:latest
RUN apt-get update
RUN apt-get -y install curl gnupg
RUN curl -sL https://deb.nodesource.com/setup_11.x  | bash -
RUN apt-get -y install nodejs

# Create app directory
WORKDIR /app/server

RUN apt-get update
RUN apt-get install software-properties-common -y
RUN add-apt-repository ppa:deadsnakes/ppa
RUN apt-get update
RUN apt-get install python3.6
RUN python3 --version
RUN apt-get install python3-pip -y      
RUN pip3 --version
RUN pip3 install pytube
RUN pip3 install tensorflow
RUN pip3 install numpy
RUN pip3 install scipy
RUN pip3 install opencv-python
RUN pip3 install pillow
RUN pip3 install matplotlib
RUN pip3 install h5py
RUN pip3 install keras
RUN pip3 install https://github.com/OlafenwaMoses/ImageAI/releases/download/2.0.2/imageai-2.0.2-py3-none-any.whl
ADD https://github.com/OlafenwaMoses/ImageAI/releases/download/1.0/yolo.h5 /app/neural/
RUN pip3 install opencv-python
RUN pip3 install opencv-contrib-python
RUN apt-get install libsm6 libxext6 libxrender-dev -y

# Install app dependencies
# A wildcard is used to ensure both package.json AND package-lock.json are copied
# where available (npm@5+)
COPY server/package*.json /app/server/

RUN npm install
# If you are building your code for production
# RUN npm ci --only=production

# Bundle app source
COPY server/. /app/server/
COPY main.py /app/
COPY arguments.py /app/
COPY downloader/. /app/downloader/
COPY image/. /app/image/
COPY video/. /app/video/

# ADD https://github.com/OlafenwaMoses/ImageAI/releases/download/1.0/yolo.h5 /app/neural/

CMD [ "node", "index.js" ]
EXPOSE 3000