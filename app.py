from flask import Flask, render_template, request, flash
from flask import send_file
import datetime
import os

app = Flask(__name__)
app.secret_key = "secretkey"

USERNAME = "admin"
PASSWORD = "liem0507z"

# Create a CSV file + headers if the file does not already exist.
if not os.path.exists("login.csv"):
    with open("login.csv", "w") as f:
        f.write("time,ip,user,status,code\n")


@app.route("/")
def home():
    return render_template("login.html")


@app.route("/login", methods=["POST"])
def login():

    username = request.form["username"]
    password = request.form["password"]

    ip = request.remote_addr
    time = datetime.datetime.now()

    if username == USERNAME and password == PASSWORD:

        with open("login.csv", "a") as f:
            f.write(f"{time},{ip},{username},SUCCESS,200\n")

        return render_template("success.html")

    else:

        with open("login.csv", "a") as f:
            f.write(f"{time},{ip},{username},FAILED,401\n")

        flash("Login failed!")

        return render_template("login.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)