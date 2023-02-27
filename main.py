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
def ytvideosize(n):
  yt = YouTube(f"http://youtube.com/watch?v={n}")
  streams = yt.streams.filter(file_extension='mp4').order_by("resolution")
  final = ""
  for i in streams:
    stri = str(i).split()
    itag = stri[1][6:-1]
    res = stri[3][5:-1]
    size = i.filesize_mb
    final += f"Video res: {res}, itag: {itag}, Video size: {size}mb <br />"
  return json.dumps(final)

@app.route("/yt/video/resolution/<string:n>/")
def ytvideoresolution(n):
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

@app.route('/yt/video/download/<string:videoid>/<int:itag>/')
def ytvideodownload(videoid,itag):
    yt = YouTube(f"http://youtube.com/watch?v={videoid}")
    video = streams = yt.streams.get_by_itag(itag)
    download = video.download()
    return send_file(download)

if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
