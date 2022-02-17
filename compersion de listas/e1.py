#first way
list_ = []

for letter in 'javascript':
    list_.append(letter)


#second wall
liist_2 = [letter for letter in 'javascript']


#first way
list_3 = []
for num in range(0,11):
    list_3.append(num**2)


#second way
list_4 = [num**2 for num in range(0,11)]


list_5 = []
for number in range(0,11):
    if number % 2 == 0:
        list_5.append(number)
    

#second way 
list_6 = [number for number in range(0,11) if number % 2 == 0]


