#!/usr/bin/python3
"""script that takes in an argument
and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument."""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host='localhost',
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3])
    cur = db.cursor()
    query = "SELECT * FROM `states` WHERE `name`='{}'"
    query = query.format(argv[4])

    cur.execute(query)
    res = cur.fetchall()
    for i in res:
        print(i)
    cur.close()
    db.close()
