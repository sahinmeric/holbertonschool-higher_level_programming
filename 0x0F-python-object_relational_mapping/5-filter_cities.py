#!/usr/bin/python3
"""script that takes in the name of a state as an argument
and lists all cities of that state, using the database hbtn_0e_4_usa
"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host='localhost',
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3])
    cur = db.cursor()
    cur.execute("SELECT cities.name FROM cities\
                RIGHT JOIN states ON states.id = cities.id\
                WHERE states.name = %s\
                ORDER BY cities.id", [argv[4]])
    res = cur.fetchall()
    newList = []
    for row in res:
        newList.append(row[0])
    print(", ".join(newList))
    cur.close()
    db.close()
