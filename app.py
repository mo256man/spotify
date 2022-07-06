from flask import Flask, render_template, request
import random
import json
from mySpotify import *

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("spotify.html")

@app.route("/call_from_ajax", methods = ["POST"])
def callfromajax():
    if request.method == "POST":
        # ここにPythonの処理を書く
        try:
            artist_name = request.form["data"]
            dict = getTopSongs(artist_name)    
        except Exception as e:
            message = str(e)
            dict = {"answer": message}
        # print(dict)
    return json.dumps(dict)


if __name__ == "__main__":
    app.run(debug=True)