from flask import Flask, request
import requests
import os
import json
app = Flask(__name__)

Token = os.environ["TOKEN"]
#url = f"https://api.telegram.org/bot{token}/sendMessage"
#url = f'http://0.0.0.0:8081/bot{token}/sendMessage'

import subprocess
@app.route('/run-script')
def run_script():
    # Execute the shell script file
    result = subprocess.run(['sh', 'my.sh'], stdout=subprocess.PIPE)

    # Get the output from the script
    output = result.stdout.decode('utf-8')

    # Return the output to the user
    return output

import telegram
from telegram.ext import Updater, CommandHandler

# Create a function to handle the /start command
def start(update, context):
    # Get the chat ID of the user who sent the message
    chat_id = update.message.chat_id
    
    # Send a welcome message
    context.bot.send_message(chat_id=chat_id, text="Hello, welcome to my bot!")
    
# Create an instance of the Updater class with your bot's token
updater = Updater(token=Token, base_url = 'http://0.0.0.0:8081')

# Create a CommandHandler for the /start command
start_handler = CommandHandler('start', start)

# Add the start_handler to the Updater's dispatcher
updater.dispatcher.add_handler(start_handler)

# Start polling for updates
updater.start_polling()

# Run the bot until you press Ctrl-C
updater.idle()


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
