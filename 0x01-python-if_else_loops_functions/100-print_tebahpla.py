#!/usr/bin/python3
for alp in range(ord('z'), ord('a') - 1, -1):
    print("{}".format((chr(alp - 32) if alp % 2 != 0 else chr(alp))) , end='')
