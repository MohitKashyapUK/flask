from flask import Flask, send_file
import os
from pytube import YouTube

app = Flask(__name__)

@app.route('/<string:n>')
def index(n):
    yt = YouTube(f"http://youtube.com/watch?v={n}")
    video = streams = yt.streams.get_highest_resolution()
    return video.download()

if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
