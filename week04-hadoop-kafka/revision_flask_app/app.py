from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return "Docker Flask App is running successfully!"
