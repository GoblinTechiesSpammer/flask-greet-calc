from flask import Flask

app = Flask(__name__)

@app.route('/welcome')
def welcome():
    #print("welcome")
    return "welcome"

@app.route('/welcome/home')
def welcome_home():
    #print("welcome home")
    return "welcome home"

@app.route('/welcome/back')
def welcome_back():
    #print("welcome back")
    return "welcome back"