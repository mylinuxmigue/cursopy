import os
def add(x,y):
    return x+y

def substract(x,y):
    return x-y

def multiply(x,y):
    return x*y

def divide(x,y):
    return x/y

operations_dictionary ={'+':add,
                        '-':substract,
                        '*':multiply,
                        '/':divide}

symbol_list = ['+','-','*','/']

for _ in range(0,3):

    symbol = input('Select an operation from the dictionary: ')

    if symbol in symbol_list:
        calculation_funtion = operations_dictionary[symbol]

        x= int(input("type a number: "))
        y= int(input("type another number: "))

        result = calculation_funtion(x,y)
        print(result)
    elif symbol not in symbol_list:
        print('invalid symbol')

    os.system('cls') 