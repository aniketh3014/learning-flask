from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

registrants = {}

@app.route("/register", methods=["POST"])
def register():
    name = request.form.get("name")
    sport = request.form.get("sport")
    registrants[name] = sport
    return render_template("success.html")

@app.route("/registered")
def registered():
    return render_template("registered.html", registered=registrants)