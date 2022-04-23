#!/usr/bin/python3
"""
Python script that takes in a URL and an email,
sends a POST request to the passed URL with the email as a parameter,
and displays the body of the response (decoded in utf-8)
"""
from urllib import request, parse
from sys import argv

if __name__ == "__main__":
    value = {'email': argv[2]}
    data = parse.urlencode(value).encode()
    req = request.Request(argv[1], data=data)
    with request.urlopen(req) as response:
        mail = response.read()
    print(mail.decode('utf-8'))
