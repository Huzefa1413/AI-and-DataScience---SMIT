from flask import Flask, render_template, request
from pymongo import MongoClient

app = Flask(__name__)
# Connect to MongoDB
client = MongoClient(
    "mongodb+srv://huzefa1413:murtaza1413@ecommerceapp.fxfigx3.mongodb.net/test"
)
db = client["Flask"]
collection = db["Users"]


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/getuser", methods=["GET"])
def getuser():
    return (
        "Hello, Your email is "
        + request.args.get("email")
        + ". Your Password is "
        + request.args.get("password")
    )


@app.route("/postuser", methods=["POST"])
def postuser():
    return (
        "Hello, Your email is "
        + request.form["email"]
        + ". Your Password is "
        + request.form["password"]
    )


app.run(debug=True)
