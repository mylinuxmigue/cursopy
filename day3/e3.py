import random

list1 = []
list1.append(1)
list1.append('hello')
list1.extend([8,9,5,'hola bebe'])
list1.append(random.randint(1,10))
#dentro de la lista viene un random que
#selecciona dentro de un intervalo un valor aleatorio
print(list1)



name_string = input("Give the names separated by ',' ")
names = name_string.split(",")
print(names)    
