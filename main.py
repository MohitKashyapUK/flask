from flask import Flask, send_file
import os
from pytube import YouTube

app = Flask(__name__)

@app.route("/ggstreams/<string:n>")
def streams(n):
  yt = YouTube(f"http://youtube.com/watch?v={n}")
  streams = yt.streams.filter(file_extension="mp4").order_by("resolution")
  x = []
  for i in streams:
    value = str(i).split()[3][5:]
    if value not in x:
      x.append(value)
  x = x.split('"')
  return x

@app.route('/video/<string:n>/<string:g>')
def video(n,g):
    yt = YouTube(f"http://youtube.com/watch?v={n}")
    video = streams = yt.streams.get_by_resolution(g)
    download = video.download()
    return send_file(download)

if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
