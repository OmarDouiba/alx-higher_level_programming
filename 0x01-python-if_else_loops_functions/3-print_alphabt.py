#!/usr/bin/python3
for alp in range(ord('a'), ord('{')):
        if chr(alp) not in ['e', 'q']:
            print("{}".format(chr(alp)), end='')
