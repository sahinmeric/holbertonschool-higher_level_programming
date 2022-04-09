#!/usr/bin/python3
"""
This script that prints the State object
with the name passed as argument from the database hbtn_0e_6_usa
"""

from sys import argv
from unicodedata import name

from requests import Session
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine(
                           "mysql+mysqldb://{}:{}@localhost/{}"
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    ses = Session()
    res = ses.query(State).filter(
                    State.name == argv[4]).order_by(State.id).all()
    if not res:
        print("Not found")
    else:
        for item in res:
            print("{}: {}".format(item.id, item.name))
    ses.close()
