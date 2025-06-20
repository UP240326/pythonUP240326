#Level 1
# Ejercicio 1
empty_list = []
# Ejercicio 2
items = ['jabon', 'lapiz', 'ropa', 'tenis', 'lapto' , 'escritorio']
# Ejercicio 3
print("Caracteres de la lista", len(items))  # Imprime la longitud de la lista
# Ejercicio 4
first_item = items[0] # Obtiene el primer elemento de la lista
middle_item = items[len(items) //2] # Obtiene el elemento del medio de la lista
last_item = items[-1] # Obtiene el último elemento de la lista
print("Primer item:",first_item)  # Imprime el primer elemento
print("Item de enmedio:",middle_item)  # Imprime el elemento del medio
print("Ultimo item:",last_item)  # Imprime el último elemento
# Ejercicio 5
mixed_data_types = ['Cristian', 18, 1.75, 'soltero', 'Calle F. Villa 106']  # Los strings van entre comillas y la lista va entre []
print("Datos personales:", mixed_data_types)
# Ejercicio 6
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
# Ejercicio 7
print("Compañías populares:", it_companies)
# Ejercicio 8
print("Número de compañías:", len(it_companies))
# Ejercicio 9
# Lista de compañías de tecnología
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

# Obtener la primera compañía
first_company = it_companies[0]

# Obtener la compañía del medio
middle_index = len(it_companies) // 2  # Divide el total de elementos entre 2
middle_company = it_companies[middle_index]

# Obtener la última compañía
last_company = it_companies[-1]

# Imprimir resultados
print("Primera compañía:", first_company)
print("Compañía del medio:", middle_company)
print("Última compañía:", last_company)

# Ejercicio 10
it_companies[1] = 'Alphabet'
print("Lista modificada:", it_companies)
# Ejercicio 11
it_companies.append('Netflix')
print("Lista después de agregar Netflix:", it_companies)
# Ejercicio 12
middle_index = len(it_companies) //2
it_companies.insert(middle_index, 'Tesla')
print("Lista después de agregar Tesla en el medio:", it_companies)
# Ejercicio 13
Apple= 'Apple'
index_of_apple = it_companies.index(Apple)
it_companies[index_of_apple] = it_companies[index_of_apple].upper()
print("La lista con 'Apple' en mayusculas es:", it_companies)
#Ejercicio 14
joined_companies= '#'.join(it_companies)
print("Compañías unidas por '#':", joined_companies)
# Ejercicio 15
company_to_check= 'Google'
exist= company_to_check in it_companies
print(f"¿Existe {company_to_check} en la lista? {exist} ")
# Ejercicio 16
it_companies.sort()
print("Lista de compañías ordenada alfabéticamente:", it_companies)
# Ejercicio 17
it_companies.reverse()
print("Lista de compañías en orden inverso:", it_companies)
# Ejercicio 18
short_list = it_companies[:3]
print("Lista de las tres primeras compañías:", short_list)
# Ejercicio 19
last_list= it_companies[-3:]
print("Lista de las tres últimas compañías:", last_list)
# Ejercicio 20
length = len(it_companies)
middle_index = len(it_companies) // 2
middle_items = it_companies[middle_index:middle_index + 1]  # Saca 1 elemento del medio
print("Compañía(s) del medio:", middle_items)
# Ejercicio 21
del it_companies[0]  # Elimina el primer elemento
print("Lista después de eliminar la primera compañía:", it_companies)
# Ejercicio 22
middle_index = len(it_companies) // 2
del it_companies[middle_index]
print("Después de eliminar la del medio:", it_companies)
# Ejercicio 23
it_companies.pop()  # o del it_companies[-1]
print("Después de eliminar la última compañía:", it_companies)
# Ejercicio 24
it_companies.clear()
print("Lista vacía:", it_companies)
# Ejercicio 25
del it_companies
# Ya no puedes imprimir la lista después de borrarla
# Ejercicio 26
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node', 'Express', 'MongoDB']
full_stack = front_end + back_end
print("Stack completo:", full_stack)
# Ejercicio 27
index_redux = full_stack.index('Redux')
full_stack.insert(index_redux + 1, 'Python')
full_stack.insert(index_redux + 2, 'SQL')

print("Full Stack con Python y SQL:", full_stack)
