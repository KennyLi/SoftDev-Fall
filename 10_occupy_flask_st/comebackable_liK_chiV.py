#Kenny Li
#SoftDev1 pd8
#K08 -- Fill Yer Flask
#2018-09-20'''

from flask import Flask, render_template
app = Flask(__name__)

import csv
import random

with open('data/occupations.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    data = []
    for row in csv_reader:
        data.append(row)

def weightedRandom():
    d = dict(data)

    total = float(d['Total']) #sets total to total percentage
    randFloat = round(random.uniform(0,total-.1), 1) #creates random float btwn 0, 99.7 inclusive

    if 'Total' in d: #deletes the total key
        del d['Total']

    if 'Job Class' in d: #deletes the job class key
        del d['Job Class']

    sum = 0.0
    for percentage in d: #continuously adds the percentage
        sum += float(d[percentage])
        if(round(sum, 1)) > randFloat: #returns 1st percentage that exceeds the randomly generated float
            return percentage

@app.route("/occupations")
def render():
    return render_template('occupations.html',
                            dataList = data,
                            weighted = weightedRandom()) 

if __name__ == "__main__":
    app.debug = True;
    app.run()