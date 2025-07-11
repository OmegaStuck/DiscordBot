from flask import Flask
from threading import Thread

app = Flask('')
@app.route('/')
def home():
    return "discord bot is working"

def run():
    app.run(hosts="0.0.0.0",port=8080)
    
def keep_alive():
    t = Thread(target=run)
    t.start()