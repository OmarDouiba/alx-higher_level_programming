#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence == "":
        tup = (0, None)
    else:
        s_len = len(sentence)
        first_ch = sentence[0]
        tup = (s_len, first_ch)
    return tup
