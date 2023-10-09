#!/usr/bin/python3
"""class MyList that inherits from list"""


class MyList(list):
    """
    subclass inherits from list class

    Methods:
        print_sorted(self): method that sort a given list
    """

    def print_sorted(self):
        """Instance method that sort a given list
        Return:
            sorted list
        """
        return print(sorted(self))

    # def print_sorted(my_list #object):
    #     return print(sorted(my_list))
