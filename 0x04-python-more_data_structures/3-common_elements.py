#!/usr/bin/python3

def common_elements(set_1, set_2):
    c_set = set (elem for elem in set_1 if elem in set_2)
    return c_set
