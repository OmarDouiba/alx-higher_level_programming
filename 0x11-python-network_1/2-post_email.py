#!/usr/bin/python3
"""
Python script that takes in a URL and an email,
sends a POST request to the passed URL with
the email as a parameter, and displays
the body of the response (decoded in utf-8)
"""
from urllib.request import urlopen
from urllib.parse import urlencode
from sys import argv


if __name__ == "__main__":
    params = {"email": argv[2]}
    queryString = urlencode(params)
    url = argv[1] + "?" + queryString

    with urlopen(url) as response:
        html = response.read().decode("utf-8")

    print("Your email is: {}".format(argv[2]))
