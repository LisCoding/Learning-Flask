from flask import Flask, render_template, session, request, redirect
app = Flask(__name__)
app.secret_key = "ThisIsSecret"

@app.route('/')
def index():
    session['counter'] += 1
    return render_template("index.html")

@app.route("/add2", methods=["POST"])
def add():
    session['counter']+= 2
    return render_template("add2.html")

@app.route("/reset", methods=["POST"])
def reset_Session():
    session['counter'] = 1
    return render_template("reset.html")

app.run(debug= True)
