#Level 1
#Ejercicio 1
empty_tuple=()
#Ejericio 2
sisters=("Eymmi", "Lizeth")
brothers=("Brayan", "Eduardo")
#Ejercicio 3
siblings = sisters + brothers
#Ejercicio 4
print (len(siblings))
#Ejercicio 5
family_members=("Mama", "papa")+siblings
#Level 2
#Ejercicio 1
*siblings, mama, papa= family_members
#Ejercicio 2
fruits = ('manzana', 'plátano', 'uva')
vegetables = ('zanahoria', 'brócoli', 'lechuga')
animal_products = ('leche', 'huevo', 'queso')
#Ejercicio 3
food_stuff_tp= fruits + vegetables + animal_products
food_stuff_tp= list(food_stuff_tp)
#Ejercicio 4
print(len(food_stuff_tp))
#Ejercicio 5
middle_index= len(food_stuff_tp)//2
print("Elementos del centro:" [middle_index +1 : middle_index -1])
#Ejercicio 6
first_t= len(food_stuff_tp)
print("Primeros 3 elementos:" (first_t [:3]))
print("ultimos 3 elementos" (first_t[-3:]))
#Ejercicio 7
del(food_stuff_tp)
#Ejercicio 8
nordic_countries = ('Denmark', 'Finland', 'Iceland', 'Norway', 'Sweden')
print('Estonia' in nordic_countries)  # False
print('Iceland' in nordic_countries)  # True





