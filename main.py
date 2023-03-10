from flask import Flask, request
import requests
import os
import json
app = Flask(__name__)
import subprocess
token = os.environ["TOKEN"]
#url = f"https://api.telegram.org/bot{token}/sendMessage"
url = f'http://localhost:8081/bot{token}/sendMessage'

from googleapiclient.discovery import build

# Your API key here
api_key = "AIzaSyCVz6d4TuCSaUWv-mytF0-kg1yJvyMq-nk"

# YouTube API client
youtube = build('youtube', 'v3', developerKey=api_key)

# Create a new comment
def add_comment(youtube, video_id, comment):
    # Insert a new top-level comment
    insert_result = youtube.commentThreads().insert(
        part="snippet",
        body={
            "snippet": {
                "videoId": video_id,
                "topLevelComment": {
                    "snippet": {
                        "textOriginal": comment
                    }
                }
            }
        }
    ).execute()

    # Print the new comment's details
    print("Comment '{}' posted in video '{}'".format(
        insert_result["snippet"]["topLevelComment"]["snippet"]["textOriginal"],
        insert_result["snippet"]["videoId"]
    ))

@app.route("/add/<string:n>")
def add(n):
  id = n
  while 0<10:
    add_comment(youtube, id, "Hey! This is python testing for you!!!")
  return "ok"

@app.route("/run")
def run():
  res = str(request.get_json()).split()
  #return str(subprocess.call(["bash","my.sh"]))
  return str(subprocess.check_output(res))
  #return res

@app.route("/uname")
def uname():
  return str(subprocess.check_output(["uname","-a"]))

@app.route("/unames")
def unames():
  return str(subprocess.check_output(["cat", "/etc/debian_version"]))

@app.route("/set")
def set():
  res = requests.get(f"http://localhost:8081/bot{token}/setWebhook",data={"url":"https://web-production-692d.up.railway.app/webhook"})
  return str(res.content)

@app.route("/webhook", methods = ["GET", "POST"])
def webhook():
  data = request.get_json()
  message_id = data["message"]["message_id"]
  chat_id = data["message"]["chat"]["id"]
  message = data["message"].get("text")
  document = data["message"].get("document")
  photo = data["message"].get("photo")
  audio = data["message"].get("audio")
  # file_id = data["message"].get("document")["file_id"]
  if message:
    requests.post(url,data={"chat_id":chat_id,"text":"Text!"})
  elif document:
    requests.post(url,data={"chat_id":chat_id,"text":"Document!"})
    '''file_id = data["message"].get("document")["file_id"]
    file_res = requests.post(f"https://api.telegram.org/bot{TOKEN}/getFile?file_id={file_id}")
    file_path = file_res["result"]["file_path"]
    file_url = f"https://api.telegram.org/file/bot{TOKEN}/{file_path}"
    requests.post(f"https://api.telegram.org/bot{token}/sendDocument",data={"chat_id":chat_id,"document":file_url})'''
  elif photo:
    json_reply_markup = json.dumps({"inline_keyboard":[[{"text":"PNG",'callback_data':'hello'},{'text':'JPEG','callback_data':'hey'}]]})
    requests.post(url,data={"chat_id":chat_id,'text':'Convert image format!',"reply_to_message_id":message_id,"reply_markup":json_reply_markup})
  elif audio:
    requests.post(url,data={"chat_id":chat_id,"text":"Audio!"})
  else:
    print(data)
    requests.post(url,data={"chat_id":chat_id,"text":"Other!"})
  return {"ok":True}
if __name__ == "__main__":
  app.run(port=os.getenv("PORT", default=5000))
