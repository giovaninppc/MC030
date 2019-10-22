from flask import Flask
import utils
import os

app = Flask(__name__)


@app.route("/<url>/<frame_by_frame_flag>")
def hello(url, frame_by_frame_flag):
    utils.downloadVideo(f'https://www.youtube.com/watch?v={url}')
    utils.processVideo('temp.mp4', frame_by_frame_flag)
    return f"DOING YOUR SHIT at https://www.youtube.com/watch?v={url}"


if __name__ == "__main__":
    # Only for debugging while developing
    app.run(host='0.0.0.0', debug=True, port=80)
