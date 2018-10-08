#RemoteError (Susan Lin & Kenny Li)
#SoftDev1 pd8
#K17 Average
#2018-10-05

import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O

DB_FILE="discobandit.db"

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops

#======================== ROUND 1 =========================

with open("data/peeps.csv") as csvfile:
    reader = csv.DictReader(csvfile)
    c.execute("CREATE TABLE IF NOT EXISTS peeps(name TEXT, age INTEGER, id INTEGER)")
    for row in reader:
        c.execute("INSERT INTO peeps VALUES(" + "'" + row["name"] + "'"  + "," + row["age"] + "," + row["id"] + ")")

#======================== ROUND 2 =========================

with open("data/courses.csv") as csvfile:
    reader = csv.DictReader(csvfile)
    c.execute("CREATE TABLE IF NOT EXISTS courses(code TEXT, mark INTEGER, id INTEGER)")
    for row in reader:
        c.execute("INSERT INTO courses VALUES(" + "'" + row["code"] + "'"  + "," + row["mark"] + "," + row["id"] + ")")

#==========================================================

dictData = {}    
#fills dictionary with name as key and value as a list of [id, grade]
def fillDict():
    data = c.execute("SELECT name, peeps.id, mark FROM peeps, courses WHERE peeps.id = courses.id")
    for row in data:
        #if name not in dictionary creates a key value pair
        if row[0] not in dictData:
            listIdGrade = [row[1], row[2]]
            dictData[row[0]] = listIdGrade
        #adds grade onto corresponding student
        else:
            dictData[row[0]][1] += row[2]
    computeAverage()

#computes average of student's grade
def computeAverage():
    for key in dictData:
        counter = 0.0
        data = c.execute("SELECT name, mark FROM peeps, courses WHERE peeps.id = courses.id")
        for row in data:
            if key == row[0]:
                counter += 1
        dictData[key][1] = dictData[key][1] / counter

#displays name, id and average from dictionary
def displayDict():
    retStr = ""
    for key in dictData:
        retStr += "Name:" + key + ", Id:" + str(dictData[key][0]) + ", Avg:" + str(dictData[key][1]) + "\n"
    return retStr

#fills peeps_avg with values from dictionary
def fillDatabase():
    c.execute("CREATE TABLE IF NOT EXISTS {0}({1}, {2}, {3})".format("peeps_avg", "name", "id", "avg"))
    for key in dictData:
        c.execute("INSERT INTO peeps_avg VALUES(?,?,?)", (key, dictData[key][0], dictData[key][1]))

#adds courses based on parameters given
def addCourse(code, mark, id):
    c.execute("INSERT INTO courses VALUES(?,?,?)", (str(code), int(mark), int(id)))

fillDict()
print (displayDict())
fillDatabase()
addCourse("biology", 100, 1)

db.commit() #save changes
db.close()  #close database

