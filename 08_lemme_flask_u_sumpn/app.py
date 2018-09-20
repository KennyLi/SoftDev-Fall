'''Kenny Li
   SoftDev1 pd8
   K08 -- Fill Yer Flask
   2018-09-20'''

from flask import Flask
app = Flask(__name__)

@app.route("/")
def start():
    return '<a href="/a"> Step 1: Get on N train </a> <br> \
    <img src ="https://upload.wikimedia.org/wikipedia/commons/thumb/7/78/NYCS-bull-trans-N.svg/400px-NYCS-bull-trans-N.svg.png">'

@app.route("/a")
def a():
    return '<a href="/b"> Step 2: Transfer to 2/3 train </a> <br> \
    <img src ="https://upload.wikimedia.org/wikipedia/commons/thumb/b/b7/NYCS-bull-trans-2.svg/400px-NYCS-bull-trans-2.svg.png">'

@app.route("/b")
def b():
    return '<a href="/c"> Step 3: ??? </a> <br> \
    <img src ="https://files1.structurae.de/files/photos/1/20080617/dsc04703_shift.jpg">'

@app.route("/c")
def c():
    return '<a href="/"> Step 4: Profit </a>'

app.debug = True;
app.run()

if __name__ == "__main__":
    app.debug = True;
    app.run()