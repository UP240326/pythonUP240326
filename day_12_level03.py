import random

# Día 12 - Nivel 3

def shuffle_list(lst):
    shuffled = lst[:]
    random.shuffle(shuffled)
    return shuffled

def unique_random_numbers():
    return random.sample(range(10), 7)
