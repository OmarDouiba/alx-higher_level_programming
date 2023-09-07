#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    argc = len(sys.argv) - 1
    if argc < 1:
        print("{} argument.".format(argc))
    elif argc == 1:
        print("{} argument:".format(argc) +
                "\n{}: {}".format(sys.argv.index(sys.argv[1]), sys.argv[1]))
    else:
        print("{} arguments:".format(argc))
        for i in range(1, len(sys.argv)):
            print("{}: {}".format(i, sys.argv[i]))
