#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    if value not in a_dictionary.values():
        return a_dictionary
    for ky, val in sorted(a_dictionary.items()):
        if value == val:
            a_dictionary.pop(ky)
    return a_dictionary
