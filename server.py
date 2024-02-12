from flask import Flask, send_from_directory, redirect

app = Flask(__name__)


@app.route("/<path:path>")
def homepage(path):
    return send_from_directory("static", path)


@app.route("/")
def index():
    return redirect("/index.html")


if __name__ == "__main__":
    app.run(host="192.168.29.49", port=8080)