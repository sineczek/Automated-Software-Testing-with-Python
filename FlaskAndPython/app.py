from flask import Flask

app = Flask(__name__)


@app.route("/mysite")  # rejestracja endpointa
def hello():
    return "Hello, world!"
