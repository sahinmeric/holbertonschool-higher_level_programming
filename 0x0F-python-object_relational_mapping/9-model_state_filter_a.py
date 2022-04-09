#!/usr/bin/python3
"""
This script that lists all State objects
that contain the letter a from the database hbtn_0e_6_usa
"""

from sys import argv

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
    sess = Session()
    result = sess.query(State).filter(
             State.name.like('%a%')).order_by(State.id).all()

    for item in result:
        print("{}: {}".format(item.id, item.name))
    sess.close()
