from flask import Flask, request
import requests
import os
import json
app = Flask(__name__)

token = os.environ["TOKEN"]
url = f"https://api.telegram.org/bot{token}/sendMessage"
#base_url = f'{request.host_url}/bot{token}/sendMessage'
host_urls = request.host_url

@app.route("/webhook", methods = ["GET", "POST"])
def webhook():
  '''data = request.get_json()
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
  elif photo:
    requests.post(url,data={"chat_id":chat_id,"text":"Photo!"})
  elif audio:
    requests.post(url,data={"chat_id":chat_id,"text":"Audio!"})
  else:
    print(data)
    requests.post(url,data={"chat_id":chat_id,"text":"Other!"})'''
  '''
  file_res = requests.get(f"https://api.telegram.org/bot{TOKEN}/getFile?file_id={file_id}")
  file_path = file_res["result"]["file_path"]
  file_url = f"https://api.telegram.org/file/bot{TOKEN}/{file_path}"
  '''
  return str(host_urls)
if __name__ == "__main__":
  app.run()
