#!/usr/bin/python3
"""add_item module"""
import sys
import os
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file


def add_item():
    """Function That add two arguments to a python list and save the them"""

    if os.path.exists("./add_item.json"):
        li = load_from_json_file("add_item.json")
        for arg in sys.argv[1:]:
            li.append(arg)
        save_to_json_file(li, "add_item.json")
    else:
        li = []
    save_to_json_file(li, "add_item.json")


if __name__ == "__main__":
    add_item()
