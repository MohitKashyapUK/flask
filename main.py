from flask import Flask, request
import requests
import os
import json
import random
app = Flask(__name__)

token = os.environ["TOKEN"]
url = f"https://api.telegram.org/bot{token}/sendMessage"

@app.route("/webhook", methods = ["GET", "POST"])
def webhook():
  data = request.get_json()
  print(data)
  """message = data["message"]["text"]
  chat_id = data["message"]["chat"]["id"]
  message_id = data["message"]["message_id"]
  text_list = ['ok','hello!','namaste!','sasriakaal','we are working on this bot!']
  def getrandomtext():
    return random.randint(0,4)
  if message == '/start':
    requests.post(url,data={"chat_id": chat_id, 'text': text_list[getrandomtext()]})
  else:"""
  #requests.post(url,data={"chat_id": chat_id, 'text': 'Hey!'})
  return {'ok':True}
if __name__ == "__main__":
  app.run(debug=True)
