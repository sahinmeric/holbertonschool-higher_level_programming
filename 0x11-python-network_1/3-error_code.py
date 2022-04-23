#!/usr/bin/python3
"""
Python script that takes in a URL,
sends a request to the URL and displays the body
of the response (decoded in utf-8).
"""
from urllib import request, error
from sys import argv

if __name__ == "__main__":
    req = request.Request(argv[1])
    try:
        with request.urlopen(req) as response:
            body = response.read()
            print(body.decode('utf-8'))
    except error.HTTPError as e:
        print("Error code: {}".format(e.code))
