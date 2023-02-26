from flask import Flask, send_file
import os
import json
from pytube import YouTube

app = Flask(__name__)

@app.route("/getggstreams/<string:n>")
def streams(n):
  yt = YouTube(f"http://youtube.com/watch?v={n}")
  streams = yt.streams.filter(file_extension='mp4').order_by("resolution")
  x = ""
  for i in streams:
    x += str(i).split()[3][5:-1]
    x += " "
  c = x.split()
  c.pop()
  j = [*set(c)]
  j.sort()
  '''count = 0
  l = len(c)
  for i in range(l):
    if c[count] not in j:
      j.append(c[count])
    count + 1'''
  g = json.dumps(j)
  return g

@app.route('/video/<string:n>/<string:g>')
def video(n,g):
    yt = YouTube(f"http://youtube.com/watch?v={n}")
    video = streams = yt.streams.get_by_resolution(g)
    download = video.download()
    return send_file(download)

if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
