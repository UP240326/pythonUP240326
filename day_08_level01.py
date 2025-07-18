#Level 1
#1
dog= {}
#2
dog ['Name']= ['Lassy']
dog ['color']= ['White']
dog ['breed']= ['Husky']
dog ['legs']= [4]
dog ['age']= [8]
#3
student= {
    'first_name': 'Cristian',
    'last_name': 'Flores',
    'gender': 'male',
    'age': '18',
    'marital_status': 'Single',
    'skills': ['Python', 'JavaScript'],
    'country': 'Mexico',
    'city': 'Ags',
    'address': 'Calle F. Villa 123'
    }
#4
print(len(student))
#5
print((student)['Skills'])
print(type(student['skills']))
#6
student['skills'].append['HTML']
student['skills'].append['CSS']
#7
print(list(student.keys()))
#8
print(list(student.value()))
#9
print(list(student.items()))
#10
del(student['marital_status'])
#11
del(student)