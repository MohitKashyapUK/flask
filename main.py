from flask import Flask, send_file
import os
import json
from pytube import YouTube

app = Flask(__name__)

@app.route("/")
def index():
  return "<b style='font-size: 50px;'>This is YouTube Video Download Bot<br />goto /yt</b>"

@app.route("/yt/")
def yt():
  o = ["/yt/streams/video_id","/yt/video/download/video_id/resolution"]
  return json.dumps(o)

@app.route("/yt/video/size/<string:n>/")
def size(n):
  yt = YouTube(f"http://youtube.com/watch?v={n}")
  streams = yt.streams.filter(file_extension='mp4').order_by("resolution")
  x = ""
  for i in streams:
    x += str(i).split()[3][5:-1]
    x += " "
  c = x.split()
  c.pop()
  o = []
  s = []
  for i in c:
    if i not in o:
      o.append(i)
  for i in o:
    k = yt.streams.get_by_resolution(str(i)).filesize_mb
    s[i] = f"{k}mb"
  return json.dumps(s)

@app.route("/yt/streams/<string:n>/")
def streams(n):
  yt = YouTube(f"http://youtube.com/watch?v={n}")
  streams = yt.streams.filter(file_extension='mp4').order_by("resolution")
  x = ""
  for i in streams:
    x += str(i).split()[3][5:-1]
    x += " "
  c = x.split()
  c.pop()
  o = []
  for i in c:
    if i not in o:
      o.append(i)
  g = json.dumps(o)
  return g

@app.route('/yt/video/download/<string:n>/<string:g>/')
def video(n,g):
    yt = YouTube(f"http://youtube.com/watch?v={n}")
    video = streams = yt.streams.get_by_resolution(g)
    download = video.download()
    return send_file(download)

if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
