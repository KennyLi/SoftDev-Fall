#Comebackable (Kenny Li & Vincent Chi)
#SoftDev1 pd8
#K10 -- Jinja Tuning
#2018-09-24M

from flask import Flask, render_template
app = Flask(__name__)

import csv
import random

with open('data/occupations.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file) #creates a csv reader object which iterates through the csv file
    data = []
    for row in csv_reader: #adds each row from the csv file into the list
        data.append(row)

def weightedRandom():
    occDict = dict(data) #converts a list into a dictionary

    total = float(occDict['Total']) #sets total to total percentage
    randFloat = round(random.uniform(0,total-.1), 1) #creates random float btwn 0, 99.7 inclusive

    if 'Job Class' in occDict: #deletes the job class key (first row)
        del occDict['Job Class']   
   
    if 'Total' in occDict: #deletes the total key (last row)
        del occDict['Total']

    sum = 0.0
    for occupation in occDict: #continuously adds the percentage into a rolling sum
        sum += float(occDict[occupation])
        if(round(sum, 1)) > randFloat: #returns 1st occupation that exceeds the randomly generated float
            return occupation

@app.route("/occupations")
def render():
    return render_template('occupations.html',
                            dataList = data,
                            weighted = weightedRandom()) 

if __name__ == "__main__":
    app.debug = True
    app.run()