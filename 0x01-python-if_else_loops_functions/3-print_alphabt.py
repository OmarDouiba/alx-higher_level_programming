#!/usr/bin/python3
for alp in range(ord('a'), ord('{')):
    if alp not in [ord('q'), ord('e')]:
        print('{}'.format(chr(alp)), end='')
