import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
 
print("Welcometo the Pypassword Generator")
nr_letters = int(input("How many letters would you like set your password?: "))
nr_numbers = int(input("How many numbers would you like set your password?: "))
nr_symbols = int(input("How many symbols would you like set your password?: "))
#Easy way
password = '' #va hacer una cadena entonces son caracteres como cadena vacia
for _ in range(1,nr_letters+1):
    #password = password + random.choice(letters) #es un intervalo abierto y lo que queremos es que imprima un valor adelante por eso el +1
    password += random.choice(letters)

for _ in range(1,nr_numbers+1):
    password += random.choice(numbers)

for i in range(1,nr_symbols+1):
    password += random.choice(symbols)

#print(f"password: {password}")

#hard way
password_list = []
for _ in range(1,nr_letters+1):
    password_list.append(random.choice(letters))

for _ in range(1,nr_numbers+1):
    password_list.append(random.choice(numbers))

for _ in range(1,nr_symbols+1):
    password_list.append(random.choice(symbols))    

random.shuffle(password_list)

final_password = ''
for element in password_list:
    final_password += element    

print(f"Password: {final_password}")

