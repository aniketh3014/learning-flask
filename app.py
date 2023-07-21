from flask import Flask, render_template, request

app = Flask(__name__)


registrants = {}

SPORTS = [
    "Basketball",
    "soccare",
    "cricket"
]

@app.route("/")
def index():
    return render_template("index.html", sports=SPORTS)


@app.route("/register", methods=["POST"])
def register():
    name = request.form.get("name")
    sport = request.form.get("sport")
    registrants[name] = sport
    return render_template("success.html")

@app.route("/registered")
def registered():
    return render_template("registered.html", registered=registrants)