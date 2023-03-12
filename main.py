from flask import Flask, request
import requests
import os
import json
app = Flask(__name__)
import subprocess
token = os.environ["TOKEN"]
#url = f"https://api.telegram.org/bot{token}/sendMessage"
url = f'http://localhost:8081/bot{token}/sendMessage'

@app.route("/pwd")
def pwd():
  return str(os.getcwd())

@app.route("/runs")
def runs():
  # update and upgrade
  subprocess.call(["apt-get", "update", "-y", "&&", "apt-get", "upgrade", "-y"])
  
  # install dependencies
  depe = "make git zlib1g-dev libssl-dev gperf cmake clang libc++-dev libc++abi-dev".split()
  for i in depe:
    try:
      subprocess.call(["apt-get","install",i,"-y"])
    except:
      return str(i)
  if os.path.exits("telegram-bot-api"):
    os.removedirs("telegram-bot-api")
    subprocess.call(["git", "clone", "--recursive", "https://github.com/tdlib/telegram-bot-api.git"])
  else:
    subprocess.call(["git", "clone", "--recursive", "https://github.com/tdlib/telegram-bot-api.git"])
  
  # telegram-bot-api
  os.chdir('telegram-bot-api')
  if os.path.exists("build"):
    # recursive
    os.removedirs("build")
    os.makedirs("build")
    os.chdir("build")
  else:
    os.makedirs("build")
    os.chdir("build")
  try:
    o = 'CXXFLAGS="-stdlib=libc++" CC=/usr/bin/clang CXX=/usr/bin/clang++ cmake -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX:PATH=.. ..'.split()
    subprocess.call(o)
  except:
    return "Error on installing flags!"
  try:
    p = "cmake --build . --target install".split()
    subprocess.call(p)
  except:
    return "Error on cmake!"
  subprocess.call(["cd", "../.."])
  subprocess.call(["./telegram-bot-api", "--api-id=$TELEGRAM_API_ID", "--api-hash=$TELEGRAM_API_HASH"])
  #subprocess.call("https://web-production-21a9.up.railway.app/")
  requests.get(f"http://localhost:8081/{token}/setWebhook",data={"url":"https://web-production-21a9.up.railway.app/webhook"})
  return "All done!"

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
  res = requests.get(f"http://localhost:8081/bot{token}/setWebhook",data={"url":"https://web-production-21a9.up.railway.app/webhook"})
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
