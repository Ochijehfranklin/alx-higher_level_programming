#!/usr/bin/python3
def no_c(my_string):
    c_less = ""
    for word in my_string:
        if word != "c" and word != "C":
            c_less += word
    return c_less

