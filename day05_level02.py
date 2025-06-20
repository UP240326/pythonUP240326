# Nivel 2
# Ejercicio 1
ages= [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
# Encontramos mínimo y máximo
min_age = min(ages)
max_age = max(ages)
print("Edades ordenadas:", ages)
print("Edad mínima:", min_age)
print("Edad máxima:", max_age)
# Añadimos de nuevo mínimo y máximo
ages.append(min_age)
ages.append(max_age)
# Volvemos a ordenar después de agregar
ages.sort()
# Longitud
n = len(ages)
# Mediana sin condicionales
# Usamos dos fórmulas: la media de dos valores centrales o uno solo
median = (ages[n//2 - 1] + ages[n//2]) / 2  # Funciona para lista par
print("Lista con min y max añadidos:", ages)
print("Mediana:", median)
# Promedio
average = sum(ages) / n
print("Promedio:", average)
# Rango
range_ages = max(ages) - min(ages)
print("Rango de edades:", range_ages)
# Diferencias entre min, max y promedio
min_diff = abs(min_age - average)
max_diff = abs(max_age - average)
print("Diferencia entre min y promedio:", min_diff)
print("Diferencia entre max y promedio:", max_diff)