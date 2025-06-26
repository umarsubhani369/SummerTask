# app.py

from flask import Flask, render_template, request
from model import ask_bot

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    user_input = request.form["user_input"]
    response = ask_bot(user_input)
    return {"response": response}

if __name__ == "__main__":
    app.run(debug=True)
