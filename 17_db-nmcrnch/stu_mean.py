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


c.execute("CREATE TABLE IF NOT EXISTS {0}({1}, {2}, {3})".format("peeps_avg", "name", "id", "avg")
    #for row in reader:
        #c.execute("INSERT INTO peeps VALUES(" + "'" + row["name"] + "'"  + "," + row["age"] + "," + row["id"] + ")")


db.commit() #save changes
db.close()  #close database
