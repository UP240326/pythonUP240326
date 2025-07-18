import random
import string

# Día 12 - Level 1

def random_user_id():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=6))

def user_id_gen_by_user():
    length = int(input("Enter the number of characters per ID: "))
    count = int(input("Enter the number of IDs to generate: "))
    for _ in range(count):
        print(''.join(random.choices(string.ascii_letters + string.digits, k=length)))

def rgb_color_gen():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return f"rgb({r},{g},{b})"



# Level 3

def shuffle_list(lst):
    shuffled = lst[:]
    random.shuffle(shuffled)
    return shuffled

def unique_random_numbers():
    return random.sample(range(10), 7)
