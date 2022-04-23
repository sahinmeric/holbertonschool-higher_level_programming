#!/usr/bin/python3
"""
Python script that fetches https://intranet.hbtn.io/status
"""
from urllib import requests

if __name__ == "__main__":
    req = requests.Request("https://intranet.hbtn.io/status")
    with requests.urlopen(req) as response:
        body = response.read()
    print("Body response:")
    print("\t- type: {}".format(type(body)))
    print("\t- content: {}".format(body))
