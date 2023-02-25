from flask import Flask, send_file
import os
from pytube import YouTube

app = Flask(__name__)

@app.route('/<string:n>/<string:g>')
def index(n,g):
    yt = YouTube(f"http://youtube.com/watch?v={n}")
    video = streams = yt.streams.get_by_resolution(g)
    download = video.download()
    return send_file(download)

if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
