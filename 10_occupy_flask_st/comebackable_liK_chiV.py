#Comebackable (Kenny Li & Vincent Chi)
#SoftDev1 pd8
#K10 -- Jinja Tuning
#2018-09-24M

from util import occupations
from flask import Flask, render_template
app = Flask(__name__)

@app.route("/occupations")
def render():
    return render_template('occupations.html',
                            dataList = occupations.data,
                            weighted = occupations.weightedRandom()) 

if __name__ == "__main__":
    app.debug = True
    app.run()