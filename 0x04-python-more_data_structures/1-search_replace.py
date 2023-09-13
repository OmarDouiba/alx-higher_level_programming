#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = []
    for i in my_list[:]:
        if i == search:
            new_list += [replace]
        else:
            new_list += [i]
    # return [replace if val == search else val for val in my_list]
    return new_list
