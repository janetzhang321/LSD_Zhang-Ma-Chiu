import sqlite3

f="discobandit.db"

db = sqlite3.connect(f)
c = db.cursor()

def getName(x):
    student = "SELECT name FROM peeps WHERE id=%d;" % x
    name = c.execute (student)
    for record in name:
        return record[0]

def getAvg(x):
    grades = "SELECT mark FROM courses, peeps WHERE peeps.id = %d AND courses.id = %d;" % (x,x)
    c.execute(grades)
    data = c.fetchall()
    total = 0;
    count = 0;
    for row in data:
        total += row[0]
        count= count + 1
    if not count == 0:
        return  total/count

def getResults():
    x = 1
    while(x < 11):
        print ("name: %s id: %d average: %d" % (getName(x), x, getAvg(x)))
        x = x+1

#print getAvg(4)
getResults()
c.close
db.close()
