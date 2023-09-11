#!/usr/bin/python3
def delete_at(my_list: list, idx=0) -> list:
    li_len = len(my_list)
    if idx < 0 or idx > li_len:
        my_list
    else:
        my_list.remove(my_list[idx])
        #del my_list[idx]
    return my_list
