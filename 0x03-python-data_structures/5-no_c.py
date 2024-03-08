#!/usr/bin/python3
def no_c(my_string):
    if my_string[:]:
        my_string1 = my_string.translate({ord("c"): None})
        new_string = my_string1.translate({ord("C"): None})
        return new_string
    return my_string
