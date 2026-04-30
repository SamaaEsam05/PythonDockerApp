from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)

def db():
    return mysql.connector.connect(host="db", user="root", password="rootpassword", database="myapp")

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        c = db()
        cur = c.cursor()
        cur.execute("INSERT INTO users (name, email) VALUES (%s, %s)", (request.form["name"], request.form["email"]))
        c.commit()
        return redirect("/")
    return render_template("home.html")

@app.route("/show")
def show():
    c = db()
    cur = c.cursor()
    cur.execute("SELECT name, email FROM users")
    return render_template("show.html", users=cur.fetchall())

app.run(host="0.0.0.0", port=5000)