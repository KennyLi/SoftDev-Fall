#Kenny Li
#SoftDev1 Pd8
#K25 -- Getting More REST
#2018-11-15

from flask import Flask, render_template, request
from urllib.request import Request, urlopen
import json
app = Flask(__name__)

@app.route("/")
def home():
    key = "https://api.pokemontcg.io/v1/cards?name=charizard"
    response = urlopen(Request(key, headers={'User-Agent': 'Mozilla/5.0'})).read()
    #print(response)
    data = json.loads(response)
    #print(data["cards"])
    #print(data["cards"][0]["name"])
    return render_template("index.html", pic = data["cards"][0]["imageUrl"], name = data["cards"][0]["name"])

if __name__ == "__main__":
    app.debug = True
    app.run()