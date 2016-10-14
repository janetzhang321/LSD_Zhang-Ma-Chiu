import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O


f="discobandit.db"

db = sqlite3.connect(f) #open if f exists, otherwise create
c = db.cursor()    #facilitate db ops

#==========================================================
#INSERT YOUR POPULATE CODE IN THIS ZONE
#...perhaps by beginning with these examples...

'''
q = "CREATE TABLE students (name TEXT, id INTEGER)"

c.execute(q)    #run SQL query


q = "CREATE TABLE courses (code TEXT, id INTEGER, mark INTEGER)"

c.execute(q)
'''

#create peeps table
q = "CREATE TABLE peeps (name TEXT,age INTEGER, id INTEGER);"
c.execute(q)    #run SQL query

#create dict
fObj = open("peeps.csv") 
d=csv.DictReader(fObj)

#add values
for k in d:
	s="INSERT INTO peeps VALUES ("+k['name']+","+k['age']+","+k['id']+");"
	c.execute(s)

#create courses table
p = "CREATE TABLE courses (code TEXT, mark INTEGER, id INTEGER);"
c.execute(p)    #run SQL query

#create dict
gObj = open("courses.csv") 
e=csv.DictReader(gObj)

#add values
for l in e:
	s="INSERT INTO courses VALUES ("+l['code']+","+l['mark']+","+l['id']+");"
	c.execute(s)


#==========================================================
db.commit() #save changes
db.close()  #close database


