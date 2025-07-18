import random
import string

# Día 12 - Nivel 2

def list_of_hexa_colors(count):
    colors = []
    for _ in range(count):
        hex_color = '#' + ''.join(random.choices('0123456789abcdef', k=6))
        colors.append(hex_color)
    return colors

def list_of_rgb_colors(count):
    return [rgb_color_gen() for _ in range(count)]

def generate_colors(type_, count):
    if type_.lower() == 'hexa':
        return list_of_hexa_colors(count)
    elif type_.lower() == 'rgb':
        return list_of_rgb_colors(count)
    else:
        return "Unsupported color type"

def rgb_color_gen():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return f"rgb({r},{g},{b})"
