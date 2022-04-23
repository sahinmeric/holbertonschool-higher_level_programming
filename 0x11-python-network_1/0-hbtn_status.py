#!/usr/bin/python3
# Python script that fetches https://intranet.hbtn.io/status
import urllib.request

if __name__ == "__main__":
    url = "https://intranet.hbtn.io/status"
    response = urllib.request.urlopen(url)
    print("Body response:")
    print("\t- type: {}".format(type(response)))
    print("\t- content: {}".format(response.read()))
    print("\t- utf8 content: {}".format(response.read().decode('utf-8')))
