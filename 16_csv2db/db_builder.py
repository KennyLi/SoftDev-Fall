#LemonSoda (Kenny Li & Johnson Li)
#SoftDev1 pd8
#K16 No Trouble
#2018-10-04

import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O

DB_FILE="discobandit.db"

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops

#======================== ROUND 1 =========================

with open("data/peeps.csv") as csvfile:
    reader = csv.DictReader(csvfile)
    c.execute("CREATE TABLE IF NOT EXISTS peeps(name TEXT, age INTEGER, id INTEGER PRIMARY KEY)")
    for row in reader:
        c.execute("INSERT INTO peeps VALUES(" + "'" + row["name"] + "'"  + "," + row["age"] + "," + row["id"] + ")")

#======================== ROUND 2 =========================

with open("data/courses.csv") as csvfile:
    reader = csv.DictReader(csvfile)
    c.execute("CREATE TABLE IF NOT EXISTS courses(code TEXT, mark INTEGER, id INTEGER, PRIMARY KEY(code, id))")
    for row in reader:
        c.execute("INSERT INTO courses VALUES(" + "'" + row["code"] + "'"  + "," + row["mark"] + "," + row["id"] + ")")

#==========================================================

db.commit() #save changes
db.close()  #close database