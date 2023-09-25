#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        for i in range(x + 1):
            print("{}".format(my_list[i]), end='')
        print('')
        return i
    except (IndexErorr):
        print('')
        return i
