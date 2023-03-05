from flask import Flask, request
import requests
import os
import json
app = Flask(__name__)

#token = os.environ["TOKEN"]
#url = f"https://api.telegram.org/bot{token}/sendMessage"

@app.route("/webhook", methods = ["GET", "POST"])
def webhook():
  """request_args = {
    "args":type(request.args),
    "argsdata":request.args,
    "data":type(request.data),
    "datadata":request.data,
    "json":type(request.json),
    "jsondata":request.json,
    "get_json":type(request.get_json()),
    "get_jsondata":request.get_json()
  }"""
  data = request.get_json()
  message = data["message"]["text"]
  chat_id = data["message"]["chat"]["id"]
  message_id = data["message"]["message_id"]
  requests.post(url,data={"chat_id": chat_id, "text": f"message: {message},\nchat_id: {chat_id},\nmessage_id: {message_id}"})
  #print(request_args)
  return {'ok':True}
if __name__ == "__main__":
  app.run(debug=True)
