#!/usr/bin/python3
for alp in range(ord('a'), ord('{')):
        if chr(alp) == 'e' or chr(alp) == 'q':
            continue
        print("{}".format(chr(alp)), end='')
