#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    count = len(sys.argv) - 1
    sum = 0

    if count == 0:
        pass
    else:
        for i in range(count):
            sum += int(sys.argv[i + 1])
    print("{}".format(sum))
