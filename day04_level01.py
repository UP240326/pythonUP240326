#Ejercicios Nivel 4
#Ejercicio 1
cadena= 'Thirty' ' ' + 'Days'' ' + 'Of' ' '+ 'Python' #Union de strings
print(cadena)
#Ejercicio 2
union = 'Coding' + ' ' + 'For' + ' ' + 'All'
print(union)
#Ejercicio 3
company = "Coding For All"
#Ejercicio 4
print(company) 
#Ejercicio 5
print(len(company)) # Longitud de la cadena
#Ejercicio 6
print(company.upper()) # Mayusculas
#Ejercicio 7
print(company.lower()) # Minusculas
#Ejercicio 8
print(company.capitalize())  # Mayuscula solo la primera letra
print(company.title())       # Mayuscula la primera letra de cada palabra
print(company.swapcase())    # Invierte las mayúsculas y minúsculas
#Ejercicio 9
print(company[7:]) #Imprime desde el caracter 7
#Ejercicio 10
print(company.find('Coding')) #Busca la palabra 'coding' y devuelve su posicion
#Se tiene que buscar con mayusculas
#Ejercicio 11
print(company.replace('Coding', 'Python')) #Reemplaza 'Coding' por 'Python'
#Ejercicio 12
pp= "Python For Everyone"
print(pp.replace('Everyone', 'All')) #Reemplaza 'Everyone' por 'All'
#Ejercicio 13
word= company.split(' ') #Divide la cadena en una lista de palabras
print(word) #Imprime la lista de palabras
#Ejercicio 14
companies= "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(companies.split(','))
#Ejercicio 15
print(companies[0]) #Imprime el primer caracter de la cadena
#Ejercicio 16
ultimo=(len(company) - 1)
print(company[ultimo]) #Imprime el ultimo caracter de la cadena
#Ejercicio 17
print(company[10]) #Imprime el caracter en la posicion 10
#Ejercicio 18
phrase = "Python For Everyone"
acronym = ''.join(word[0] for word in phrase.split())
print(acronym)
#Ejercicio 19
phrase_1 = "Coding For All"
acronym_1 = ''.join(word[0] for word in phrase_1.split())
print(acronym_1)
#Ejercicio 20
posicion= company.index('C') #Busca la posicion de la letra 'C'
print(posicion) #Imprime la posicion de la letra 'C'
#Ejercicio 21
print(company.index('F')) #Busca la posicion de la letra 'F'
#Ejercicio 22
text = "Coding For All People"
position = text.rfind('l')
print(position)
#Ejercicio 23
sentence = 'You cannot end a sentence with because because because is a conjunction'
print(sentence.index('because')) # Busca la primera ocurrencia de 'because'
#Ejercicio 24
sentence_1 = 'You cannot end a sentence with because because because is a conjunction'
position_1 = sentence_1.rindex('because')
print(position_1)
#Ejercicio 25  
oracion = 'You cannot end a sentence with because because because is a conjunction'
frase = 'because because because'
start= oracion.find(frase) #Econtramos la primera posicion
end= start + len(frase) #Sumamos la longitud de la frase
sliced= oracion[start:end] #Hacemos un slice de la cadena
print(sliced) #Imprimimos el resultado del slice
#Ejercicio 26
sentence_26 = 'You cannot end a sentence with because because because is a conjunction'
first_pos_because = sentence_26.find('because')
print(first_pos_because)
#Ejercicio 27
sentence_27 = 'You cannot end a sentence with because because because is a conjunction'
phrase_27 = 'because because because'

start_27 = sentence_27.find(phrase_27)
end_27 = start_27 + len(phrase_27)

sliced_27 = sentence_27[start_27:end_27]
print(sliced_27)
#Ejercicio 28
text_28 = 'Coding For All'
starts_with_coding = text_28.startswith('Coding')
print(starts_with_coding)
#Ejercicio 29
text_29 = 'Coding For All'
ends_with_coding = text_29.endswith('coding')
print(ends_with_coding)
#Ejercicio 30
text_30 = '   Coding For All     '
stripped_text = text_30.strip()
print(stripped_text)
#Ejercicio 31
var1 = '30 Days Of Python'
var2 = 'thirty Days Of Python' 
print(var1.isidentifier()) # Verifica si es un identificador válido
print(var2.isidentifier()) # Verifica si es un identificador válido
#Ejercicio 32
libraries = 'Django, Flask, Bottle, Pyramid, Falcon'
joined_libraries = ' # '.join(libraries)
print(joined_libraries) # Une las librerías con ' # ' como separador
#Ejercicio 33
text_3= 'I am enjoying this challenge. \nI just wonder what is next.'
print(text_3)
#Ejercicio 34
text4 = 'name\tage\tcountry\tcity\nAsabeneh\t250\tFinland\tHelsinki'
print(text4)
#Ejercicio 35
radius = 10
area = 3.14 * radius ** 2
print("The Area of the circle with radius {} is {} meters square.".format(radius, int(area)))
#Ejercicio 36)
a=8
b=6
print(f"{a} + {b} = {a+b}")
print(f"{a} - {b} = {a-b}")
print(f"{a} * {b} = {a*b}")
print(f"{a} / {b} = {a/b}")
print(f"{a} % {b} = {a%b}")
print(f"{a} // {b} = {a//b}")
print(f"{a} ** {b} = {a**b}")
#Usamos f"a{} para que el valor de a y b se imprima en la cadena