#!/usr/bin/python3
"""
Python script that fetches https://intranet.hbtn.io/status
"""
from urllib import requests

if __name__ == "__main__":
    req = requests.get("https://intranet.hbtn.io/status")
    body = req.text
    print("Body response:")
    print("\t- type: {}".format(type(body)))
    print("\t- content: {}".format(body))
