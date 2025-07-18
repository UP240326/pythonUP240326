# Día 13

# Ejercicio 1: Filtrar negativos y ceros
numeros = [-4, -3, -2, -1, 0, 2, 4, 6]
negativos_y_ceros = [n for n in numeros if n <= 0]
print(negativos_y_ceros)  # [-4, -3, -2, -1, 0]

# Ejercicio 2: Aplanar lista de listas
lista_de_listas = [[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
aplanada = [num for sublista in lista_de_listas for interna in sublista for num in interna]
print(aplanada)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Ejercicio 3: Generar tabla con operaciones
tabla = [(n, 1, n, n*2, n*3, n*4, n*5) for n in range(11)]
print(tabla)
# Resultado esperado: [(0, 1, 0, 0, 0, 0, 0), ..., (10, 1, 10, 20, 30, 40, 50)]

# Ejercicio 4: Transformar países y ciudades en mayúsculas y abreviaciones
paises = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
paises_convertidos = [[pais.upper(), pais[:3].upper(), ciudad.upper()] 
for par in paises for (pais, ciudad) in par]
print(paises_convertidos)
# [['FINLAND', 'FIN', 'HELSINKI'], ['SWEDEN', 'SWE', 'STOCKHOLM'], ['NORWAY', 'NOR', 'OSLO']]

# Ejercicio 5: Diccionarios de país y ciudad
diccionarios = [{'pais': pais.upper(), 'ciudad': ciudad.upper()} 
                for par in paises for (pais, ciudad) in par]
print(diccionarios)
# [{'pais': 'FINLAND', 'ciudad': 'HELSINKI'}, ...]

# Ejercicio 6: Nombres completos con formato
nombres = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
nombres_completos = [f"{nombre} {apellido}" for par in nombres for (nombre, apellido) in par]
print(nombres_completos)
# ['Asabeneh Yetayeh', 'David Smith', 'Donald Trump', 'Bill Gates']

# Ejercicio 7: Cálculo de pendiente con condición de división entre cero
pendiente = lambda x1, y1, x2, y2: (y2 - y1) / (x2 - x1) if x2 != x1 else 'Indefinida'
print(pendiente(2, 3, 4, 7))  # 2.0
