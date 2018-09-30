#Kenny Li
#SoftDev1 Pd8
#K13 -- Echo Echo Echo
#2018-09-27

from flask import Flask, render_template, request
app = Flask(__name__)


@app.route("/")
def home():
    return render_template("input.html")

@app.route("/auth", methods = ["GET", "POST"])
def authenticate():
    if request.method == "GET":
        return render_template("output.html", name = request.args['name'], method = request.method)
    else:
        return render_template("output.html", name = request.form['name'], method = request.method)        


if __name__ == "__main__":
    app.debug = True
    app.run()
