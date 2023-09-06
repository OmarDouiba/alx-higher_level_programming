#!/usr/bin/python3
for alp in range(ord('z'), ord('a') - 1, -1):
    if alp % 2 == 0:
        print(chr(alp), end='')
    else:
        print(chr(alp - 32), end='')
