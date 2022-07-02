import sqlite3 as sql

connection = sql.connect("dabaseMovies.db")

alex = connection.cursor()
alex.execute("CREATE TABLE IF NOT EXISTS Movies( NAME TEXT, ACTOR TEXT, ACTRESS TEXT,DIRECTOR_NAME TEXT, YEAR INTEGER )")
alex.execute("INSERT INTO Movies VALUES('Mahaan','Vikram','simbran','Karthik Subbaraj',2022)")
alex.execute("INSERT INTO Movies VALUES('Master','vijay','Malavika Mohanan','Lokesh Kanagaraj',2022)")
alex.execute("INSERT INTO Movies VALUES('Doctor','Sivakarthikeyan','Priyanka Arul Mohan','Nelsan',2022)")
alex.execute("INSERT INTO Movies VALUES('Beast','vijay','Pooja Hegde','Nelson',2022)")
alex.execute("INSERT INTO Movies VALUES('Thuppakki','vijay','Kajal Aggarwal','A R Murugadoss',2012)")

# Printing all the elements of the database
print("ALL RECORDS IN THE DATABASE TABLE")
allMovies = alex.execute("SELECT * FROM Movies").fetchall()
for m in allMovies:
  title,actor,actress,director,releasedYear = m
  print("{t}\t\t{a}\t\t{ats}\t\t{d}\t\t{ry}".format(t=title,a=actor, ats=actress,d=director,ry=releasedYear))


# In this query, we are printing only the details from the db where Tom Holland is the lead actor
print("\n\n\nSELECTED VIJAY ACTING MOVIES")
actorQuery = alex.execute("SELECT * FROM Movies WHERE ACTOR = 'vijay'").fetchall()
for m in actorQuery:
  title,actor,actress,director,releasedYear = m
  print("{t}\t\t{a}\t\t{ats}\t\t{d}\t\t{ry}".format(t=title,a=actor, ats=actress,d=director,ry=releasedYear))
