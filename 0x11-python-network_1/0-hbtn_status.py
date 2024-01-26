#!/usr/bin/python3
"""
script that fetches https://alx-intranet.hbtn.io/status
"""
from urllib.request import urlopen


if __name__ == "__main__":
    with urlopen("https://alx-intranet.hbtn.io/status") as response:
        html = response.read()
        print("Body response:")
        print("\t- type: {}\n\t- content: {}\n\t- utf8 content: {}".format(
            html.__class__,
            html,
            html.decode("UTF-8")))
