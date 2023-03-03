from flask import Flask, send_file, request
import os
import json
from pytube import YouTube

app = Flask(__name__)

@app.route("/")
def index():
  return "<b style='font-size: 50px;'>This is YouTube Video Download Bot<br />goto /yt</b>"

@app.route('/headers/')
def headers():
  return request.headers

@app.route("/yt/")
def yt():
  o = ["/yt/streams/video_id","/yt/video/download/video_id/resolution"]
  return json.dumps(o)

@app.route("/yt/video/info/<string:n>/")
def ytvideosize(n):
  yt = YouTube(f"http://youtube.com/watch?v={n}")
  streams = yt.streams.filter(file_extension='mp4').order_by("resolution")
  final = "<div style='width: 95vw;'><h1>"
  for i in streams:
    itag = i.itag
    res = i.resolution
    size = i.filesize_mb
    have_audio = i.includes_audio_track
    final += f"Video res: {res}, itag: {itag}, Video size: {size}mb, Have audio: {have_audio}<br />"
  final += "</h1></div>"
  return json.dumps(final)[1:-1]

@app.route('/yt/video/download/<string:videoid>/<int:itag>/')
def ytvideodownload(videoid,itag):
    yt = YouTube(f"http://youtube.com/watch?v={videoid}")
    video = yt.streams.get_by_itag(itag)
    url = json.dumps(f"<a style='width: 90vw;' href='{video.url}' />")
    return url

if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
