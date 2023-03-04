from flask import Flask, request
import requests
import os
import json
app = Flask(__name__)

token = os.getenviron("TOKEN")
url = f"https://api.telegram.org/bot{token}/sendMessage"

@app.route("/webhook", methods = ["GET", "POST"])
def index():
  request_args = request.args
  message = request_args["result"][0]["message"]["text"]
  chat_id = request_args["result"][0]["message"]["chat"]["id"]
  message_id = request_args["result"][0]["message"]["message_id"]
  if message == "/start":
    requests.post(url,data={"chat_id": chat_id, "text": "Start!"})
  elif message == "hello":
    requests.post(url,data={"chat_id": chat_id, "text": "Hello!"})
  else:
    requests.post(url,data={"chat_id": chat_id, "text": "Default!"})
  return json.dumps({"ok":True})

if __name__ == "__main__":
  app.run(debug=True)
