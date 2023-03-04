from flask import Flask, request
import  requests
import os
app = Flask(__name__)

token = os.environ.get("TOKEN")
url = f"https://api.telegram.org/bot{token}/sendMessage"

@app.route("/")
def index():
  request_args = request.args
  message = request_args["result"][0]["message"]["text"]
  chat_id = request_args["result"][0]["message"]["chat"]["id"]
  message_id = request_args["result"][0]["message"]["message_id"]
  switch message:
    case "/start":
      requests.post(url,data={"chat_id": chat_id, "text": "Start!"})
      break
    case "hello":
      requests.post(url,data={"chat_id": chat_id, "text": "Hello!"})
      break
    default:
      requests.post(url,data={"chat_id": chat_id, "text": "Default!"})

if __name__ == "__main__":
  app.run(debug=True)
