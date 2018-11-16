#Kenny Li
#SoftDev1 Pd8
#K26 -- Getting More REST
#2018-11-16

from flask import Flask, render_template, request
from urllib.request import Request, urlopen
import json
app = Flask(__name__)

@app.route("/")
def root():
    return render_template("index.html")

@app.route("/rest")
def rest():
    api = request.args["type"]
    if api == "football":
        key = "a5c79ef83d8c40caa20295fe4566e2c8"
        base_url = "http://api.football-data.org"
        endpoint = "/v2/competitions/2000"
        response = urlopen(Request(base_url + endpoint, headers={'X-Auth-Token': key})).read()
        data = json.loads(response)
        #print(data["currentSeason"])
        return render_template("football.html", name = data["name"],
                                             start = data["currentSeason"]["startDate"],
                                             end = data["currentSeason"]["endDate"],
                                             winner = data["currentSeason"]["winner"]["name"],
                                             crest = data["currentSeason"]["winner"]["crestUrl"])
    elif api == "number":
        base_url = "http://numbersapi.com"
        endpoint = "/random/trivia"
        response = urlopen(base_url + endpoint).read().decode("UTF-8")
        #print(response)
        return render_template("number.html", trivia = response)
    elif api == "poem":
        base_url = "https://www.poemist.com/api"
        endpoint = "/v1/randompoems"
        response = urlopen(base_url + endpoint).read().decode("UTF-8")
        data = json.loads(response)
        #print(data[0])
        #print(data[4])
        return render_template("poem.html", title = data[0]["title"], 
                                            poet = data[0]["poet"]["name"], 
                                            content = data[0]["content"])

if __name__ == "__main__":
    app.debug = True
    app.run()