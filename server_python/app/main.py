from flask import Flask
import utils
import os
from datetime import datetime

app = Flask(__name__)

@app.route("/<url>/<frame_by_frame_flag>")
def hello(url, frame_by_frame_flag):
    gotAt = datetime.now().strftime('%M:%S.%f')
    print(f"{gotAt},", file=open(name, "a"), end="")
    utils.downloadVideo(f'https://www.youtube.com/watch?v={url}')
    utils.processVideo('temp.mp4', frame_by_frame_flag)
    processedAt = datetime.now().strftime('%M:%S.%f')
    print(f"\nfinished at: {processedAt}\n")
    name = f"out.txt"
    print(f"{processedAt}", file=open(name, "a"))
    return f"Got requisition at: {gotAt}"

if __name__ == "__main__":
    # Only for debugging while developing
    app.run(host='0.0.0.0', debug=True, port=80)