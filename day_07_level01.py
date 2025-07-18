#Ejercicio 1
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
print(len(it_companies))
#2
it_companies.add("Twitter")
#3
it_companies.update(['Spotify', 'TikTok', 'Netflix'])
#4
it_companies.remove("Apple")
#5
'''Remove: Lanza error si no existe el elemento
betwen: No lanza error aunqu eno exista'''
#Level 2
#1
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 28, 27}
print(A.union(B))
#2
print(A.intersection(B))
#3
print(A.issubset(B))
#4
print(A.isdisjoint(B))
#5
print((A.union(B)).union(B.union(A)))
#6
print(A.symmetric_difference(B))
#7
del A
del B
#Level 3
#1
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
age_set= set(ages)
print(len(age_set))
print(len(ages))
#2
'''- string: texto, ejemplo: 'hola'
- list: secuencia ordenada y modificable, ejemplo: ['a', 'b', 'c']
- tuple: secuencia ordenada pero NO modificable, ejemplo: ('a', 'b', 'c')
- set: colección desordenada, sin duplicados, ejemplo: {'a', 'b', 'c'}
'''
#3
sentence = 'I am a teacher and I love to inspire and teach people.'
words= sentence.split()
unique_words= set(words)
print(len(unique_words))