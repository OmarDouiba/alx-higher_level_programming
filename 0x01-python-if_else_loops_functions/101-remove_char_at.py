#!/usr/bin/python3
def remove_char_at(str, n):
    if n > len(str) or n < 0:
        str1 = str
    else:
        str1 = ""
        for i in range(0, len(str)):
            if i == n:
                continue
            str1 += str[i]
    return (str1)
