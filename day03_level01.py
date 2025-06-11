# Ejercicio 1-3
age= int(input ("Put your age: "))
height= float(input("Put your height:"))
complex= (2j, 3j)
base= int(input("Put the base of triangle:"))
# Ejercicio 4
Print= ("We are going to calculate the area of a triangle")
height_triangle= float(input("Put the height of triangle:"))
area_of_triangle= base* height_triangle / 2
Print= ("The area of the triangle is:", area_of_triangle)
# Ejercicio 5
print ("We are going to calculate the perimeter of a triangle")
side_a= float(input("Put de side a of the triangle:"))
side_b= float(input("Put de side b of the triangle:"))
side_c= float(input("Put de side c of the triangle:"))
perimeter_of_triangle= side_a + side_b + side_c
print("The perimeter of the triangle is:", perimeter_of_triangle)
# Ejercicio 6
print("We are going to calculate the area of a rectangle")
lenght_rectangle= float(input("Put the length of the rectangle:"))
width_rectangle= float(input("Put the width of the rectangle:"))
area_of_rectangle= lenght_rectangle * width_rectangle
print("The area of the rectangle is:", area_of_rectangle)
# Ejercicio 7
print("We are going to calculate the radius of a circle")
pi= 3.14
r= float(input("Put the radius of the circle:"))
circumference_of_circle= 2 * pi * r
area_of_circle= pi*r*r
print("The circumference of the circle is:", circumference_of_circle)
print ("The area of circle is:" ,area_of_circle)
# Ejercicio 8
m = 2                     # pendiente
y_intercept = 2 * 0 - 2   # cuando x = 0
x_intercept = (0 + 2) / 2 # cuando y = 0

print("Pendiente:", m)
print("Intersección Y:", (0, y_intercept))
print("Intersección X:", (x_intercept, 0))

# Ejercicio 9
import math

x1, y1 = 2, 2
x2, y2 = 6, 10

slope = (y2 - y1) / (x2 - x1)
distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

print("Pendiente entre puntos:", slope)
print("Distancia euclidiana:", distance)
# Ejercicio 10
if slope == m:
    print("Las pendientes son iguales.")
else:
    print("Las pendientes son diferentes.")
# Ejercicio 11
def f(x):
    return x**2 + 6*x + 9

# Probar varios valores
for x in range(-6, 2):
    print(f"x = {x}, y = {f(x)}")

# Calcular en qué x, y = 0
# Sabemos que (x + 3)^2 = 0 => x = -3
print("y = 0 cuando x =", -3)
# Ejercicio 12
dragon = len("dragon")
python = len("python")
print("Longitud de la palabra 'dragon':", len("dragon"))
print("Longitud de la palabra 'python':", len("python"))
if dragon == python:
    print("Las palabras 'dragon' y 'python' tienen la misma longitud.")
else:
    print("Las palabras 'dragon' y 'python' tienen longitudes diferentes.")
# Ejercicio 13
if 'on' in 'dragon' and 'on' in 'python':
    print("'on' está en ambas palabras.")
else:
    print("'on' no está en ambas palabras.")
# Ejercicio 14
sentence= "I hope this course is not full of jargon"
if 'jargon' in sentence:
    print("La palabra 'jargon' está en la frase.")
else:
    print("La palabra 'jargon' no está en la frase.")
# Ejercicio 15
if 'on' in dragon and 'on' in python:
    print("'on' está en ambas palabras.")
else:
    print("'on' no está en ambas palabras.")
# Ejercicio 16
lenght= len(python)
print("Longitud de la palabra 'python':", lenght)
lenght_float= float(lenght)
print("Longitud de la palabra 'python' como float:", lenght_float)
lenght_str= str(lenght)
print("Longitud de la palabra 'python' como string:", lenght_str)
# Ejercicio 17
numero= int(input("Introduce un número: "))
if numero % 2 == 0:
    print("El número es par.")
else:  
    print("El número es impar.")
# Ejercicio 18
result= 7//2
int_result= int(result)
print("Resultado de 7//2 como entero:", int_result)
# Ejercicio 19
print(type("10") == type(10))
# Ejercicio 20
print( type("9.8") == type(10))
# Ejercicio 21
horas_trabajadas = int(input("Introduce las horas trabajadas: "))
pago_hora= float(input("Introduce el pago por hora: "))
sueldo = horas_trabajadas * pago_hora
print("El sueldo es:", sueldo)
# Ejercicio 22
years= int(input("Introduce los años: "))
years_max= 100
seconds_year= 60 * 60 * 24 * 365
seconds_lived = years * seconds_year
print("Has vivido aproximadamente", seconds_lived, "segundos.")
print("Si vivieras hasta los", years_max, "años, vivirías aproximadamente", years_max * seconds_year, "segundos.")
# Ejercicio 23
for i in range(1, 6):
    print(i, 1, i, i**2, i**3)