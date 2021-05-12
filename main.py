from flask import Flask, render_template

app = Flask("Flask_Hello")

@app.route("/")
def home():
  return "Hello! Welcome to mi casa!"

@app.route("/<username>")
def potato(username):
  return render_template("potato.html")

app.run(host="0.0.0.0")