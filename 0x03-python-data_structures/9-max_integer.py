#!/usr/bin/python3

def max_integer(my_list=[]):
    if len(my_list) == 0;
        return (None)

    big = my_list[0]
    for num in range(1, len(my_list)):
        if big < my_list[num]:
            big = my_list[num]
        else:
            continue

        return (big)

