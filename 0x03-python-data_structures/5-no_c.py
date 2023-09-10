#!/usr/bin/python3
def no_c(my_string: str) -> str:
    new_str = ""
    for ch in my_string:
        if ord(ch) != ord('c') and ord(ch) != ord('C'):
            new_str += ch
    return new_str
