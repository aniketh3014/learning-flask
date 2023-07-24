from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)
# use sqlite3
db = sqlite3.connect("froshims.db", check_same_thread=False)
cur = db.cursor()
registrants = {}

SPORTS = [
    "Basketball",
    "soccer",
    "cricket"
]

@app.route("/")
def index():
    return render_template("index.html", sports=SPORTS)

@app.route("/deregister", methods=["POST"])
def deregister():
    id = request.form.get("id")
    if id:
        cur.execute("DELETE FROM registrants WHERE id=?", id)
        db.commit()
    return redirect("/registered")




@app.route("/register", methods=["POST"])
def register():
    # validate submission
    name = request.form.get("name")
    sport = request.form.get("sport")
    if not name or sport not in SPORTS:
        return render_template("failure.html")

    # remember registrant
    cur.execute("INSERT INTO registrants (name, sport) VALUES(?, ?)",(name, sport))
    # confrimation
    return redirect("/registered")

@app.route("/registered")
def registered():
    cur.execute("SELECT * FROM registrants")
    rows = cur.fetchall()
    columns = ['Id', 'name', 'sport']
    result_list = [dict(zip(columns, row)) for row in rows]
    db.close
    return render_template("registered.html", registered=result_list)