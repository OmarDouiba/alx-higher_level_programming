#!/usr/bin/python3
"""add_item module"""
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


def add_item():
    js_file = save_to_json_file("add_item.json")
    data = load_from_json_file(sys.argv, "js_file")
    return (data)

if __name__ == "__main__":
    add_item()
