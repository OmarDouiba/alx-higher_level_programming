#!/usr/bin/python3
#def safe_print_integer(value):
#    try:
#        print("{:d}".format(int(value)))
#        return True
#    except (ValueError):
#        return False

def safe_print_integer(value):
    try:
        if int(value) is not str:
            print("{:d}".format(value))
            return True
    except (ValueError):
        return False
