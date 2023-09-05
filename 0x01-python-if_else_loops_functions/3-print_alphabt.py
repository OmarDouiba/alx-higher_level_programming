#!/usr/bin/python3
for alp in range(ord('a'), ord('{')):
        if chr(alp) in ['q', 'e']:
            continue
        print("{}".format(chr(alp)), end='')
