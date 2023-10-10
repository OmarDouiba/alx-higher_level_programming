#!/usr/bin/python3
"""load_from_json_file"""
import json


def load_from_json_file(filename):
    """function that creates an Object from a “JSON file”."""

    with open(filename, "r") as l_json:
        l_json = json.load(l_json)
        return (l_json)
