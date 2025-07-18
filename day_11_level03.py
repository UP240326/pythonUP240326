# Level 3
import math
from statistics import mean, median, variance, stdev
from collections import Counter

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def are_items_unique(lst):
    return len(lst) == len(set(lst))

def are_same_type(lst):
    return all(type(x) == type(lst[0]) for x in lst)

def is_valid_variable(name):
    return name.isidentifier()
