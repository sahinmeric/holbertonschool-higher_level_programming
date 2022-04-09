#!/usr/bin/python3
"""script that lists all cities from the database hbtn_0e_4_usa"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host='localhost',
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3])
    cur = db.cursor()
    cur.execute("SELECT cities.id, cities.name, states.name FROM cities\
                LEFT JOIN states ON cities.state_id = states.id\
                ORDER BY cities.id")
    res = cur.fetchall()
    for i in res:
        print(i)
    cur.close()
    db.close()
