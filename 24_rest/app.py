#Kenny Li
#SoftDev1 Pd8
#K24 -- A RESTful Journey Skyward
#2018-11-14

from flask import Flask, render_template
from urllib import request
import json
app = Flask(__name__)

@app.route("/")
def home():
    key = "https://api.nasa.gov/planetary/apod?date=2018-11-10&api_key=gpIAYj6MqHViKv7ezcm7fLB7uFykIcONmM1SpOF3"
    f = request.urlopen(key).read()
    nasaDict = json.loads(f)
    return render_template("index.html", pic = nasaDict["url"], desc = nasaDict["explanation"])

if __name__ == "__main__":
    app.debug = True
    app.run()