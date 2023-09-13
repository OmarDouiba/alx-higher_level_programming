#!/usr/bin/python3
def best_score(a_dictionary):
    val = 0
    if not a_dictionary:
        return None
    for key, value in a_dictionary.items():
        if value > val:
            val, keyD = value, key
    return keyD
