#!/usr/bin/python3
for alp in range(ord('a'), ord('{')):
    if alp != ord('q') and alp != ord('e'):
        print('{}'.format(chr(alp)), end='')
