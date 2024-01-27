#!/usr/bin/python3
"""
Python script that takes in a URL and an email,
sends a POST request to the passed URL with
the email as a parameter, and displays
the body of the response (decoded in utf-8)
"""
from urllib.request import urlopen, Request
from urllib.parse import urlencode
from sys import argv


if __name__ == "__main__":
    params = {"email": argv[2]}
    queryString = urlencode(params).encode("utf-8")
    url = Request(argv[1], queryString, method="POST")

    with urlopen(url) as response:
        info = response.read()
        print(info.decode("utf-8"))
