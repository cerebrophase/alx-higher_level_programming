#!/usr/bin/python3
""" function thaat reads a text file """


def read_file(filename=""):
    """ reads a text file(utf-8) and prints to stdout """

    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end="")
