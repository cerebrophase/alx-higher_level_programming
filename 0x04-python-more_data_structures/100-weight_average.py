#!/usr/bin/python3

def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0
    numerator = sum([score * weight for score, weight in my_list])
    denominator = sum([weight for score, weight in my_list])
    weighted_average = numerator / denominator
    return weighted_average
