#!/usr/bin/python3
"""
Python script that fetches https://intranet.hbtn.io/status
"""
import requests
from sys import argv

if __name__ == "__main__":
    req = requests.get("https://intranet.hbtn.io/status")
    body = req.text
    print("Body response:")
    print("\t- type: {}".format(type(body)))
    print("\t- content: {}".format(body))
