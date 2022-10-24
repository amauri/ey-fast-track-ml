#!/usr/bin/python3

from flask import Flask, request
import requests

app = Flask(__name__)
key = "[api key telegram]"
users = {}
text = ""



@app.route('/hello')
def hello():
    return 'Hello World'



def send_message(chat_id, text):
    url = "https://api.telegram.org/bot{}/sendMessage".format(key)
    payload = {
        "text": text,
        "chat_id": chat_id
        }
    resp = requests.get(url,params=payload)


# envia msg ao telegram para usuários que acessaram o bot
@app.route("/", methods=["POST","GET"])
def index():
    if(request.method == "POST"):
        msg_text, sender_name, sender_id, chat_id = "","","",""
        response = request.get_json()
        if 'message' in response:
            msg_text = response["message"]["text"]
            sender_name = response["message"]["from"]["first_name"]
            sender_id = response["message"]["from"]["id"]
            chat_id = response["message"]["chat"]["id"]
        print(users)
        if sender_id in users:
            text = f"{sender_name}, estamos monitorando..." 
        else:
            text = f"Olá {sender_name}!\n A partir de agora está inscrito no sistema de detecção de invasão de pombos.\
                   \nAguarde para receber o aviso quando o pombo invadir o ambiente..."
        send_message(chat_id, text)
        users[sender_id] = sender_name
    return "Done"

# envia a notificação que o pombo invadiu o ambiente
@app.route("/send", methods=["POST"])
def send_warnings():
    if(request.method == "POST"):
        if users:
            for i in users.keys():
                send_message(i, "O pombo invadiu!!!")
    return f"number of users who received the message: {len(users)}."



# Ativa a api do bot para responder no endereço(url). Utilizando ngrok.
@app.route("/activate")
def activate():
    url = "https://fc49-144-22-140-105.sa.ngrok.io"
    response = requests.get("https://api.telegram.org/bot{}/setWebhook?url={}".format(key,url))
    return "Telegram Bot activate" if response else "Fail to activate Telegram Bot"


if __name__ == "__main__":
    app.run(debug=True)
