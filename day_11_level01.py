import math
from statistics import mean, median, variance, stdev
from collections import Counter

# Día 11 - Level 1

def add_two_numbers(a, b):
    return a + b

def area_of_circle(r):
    return math.pi * r * r

def add_all_nums(*args):
    if all(isinstance(x, (int, float)) for x in args):
        return sum(args)
    return "All arguments must be numbers"

def convert_celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def check_season(month):
    month = month.lower()
    if month in ['september', 'october', 'november']:
        return 'Autumn'
    elif month in ['december', 'january', 'february']:
        return 'Winter'
    elif month in ['march', 'april', 'may']:
        return 'Spring'
    elif month in ['june', 'july', 'august']:
        return 'Summer'
    else:
        return 'Invalid month'

def calculate_slope(x1, y1, x2, y2):
    return (y2 - y1) / (x2 - x1)

def solve_quadratic_eqn(a, b, c):
    d = b ** 2 - 4 * a * c
    if d < 0:
        return "No real roots"
    elif d == 0:
        root = -b / (2 * a)
        return (root,)
    else:
        root1 = (-b + math.sqrt(d)) / (2 * a)
        root2 = (-b - math.sqrt(d)) / (2 * a)
        return (root1, root2)

def print_list(lst):
    for item in lst:
        print(item)

def reverse_list(lst):
    return lst[::-1]

def capitalize_list_items(lst):
    return [item.capitalize() for item in lst]

def add_item(lst, item):
    lst.append(item)
    return lst

def remove_item(lst, item):
    if item in lst:
        lst.remove(item)
    return lst

def sum_of_numbers(n):
    return sum(range(n + 1))

def sum_of_odds(n):
    return sum(i for i in range(n + 1) if i % 2 != 0)

def sum_of_even(n):
    return sum(i for i in range(n + 1) if i % 2 == 0)



