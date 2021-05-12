from flask import Flask, render_template, request

app = Flask("Flask_Hello")

@app.route("/")
def home():
  return render_template("potato.html")

@app.route("/report")
def report():
  word = request.args.get('word')
  return render_template("report.html", searchingBy=word, potato="awesome")

app.run(host="0.0.0.0")