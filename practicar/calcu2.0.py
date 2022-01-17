from cProfile import run
from log_cal import calcu
import os

def sum(x,y):
    return x+y
def substract(x,y):
    return x-y
def multiply(x,y):
    return x*y
def division(x,y):
    return x/y

print(calcu)

def calculator():
    operation_dictionary = {'+':sum,
                            '-':substract,
                            '*':multiply,
                            '/':division}
    x = int(input('type the first number: '))
    for key in operation_dictionary:
        print(key)

    run_again = True

    while run_again:
        symbol = input('pick an operation: ')
        symbol_list = ['+','-','*','/']
        calculation_operation = operation_dictionary[symbol]
        if symbol in symbol_list:
            
            y = int(input('type the another number:'))
            result = calculation_operation(x,y)
            print(result)
            
        elif symbol not in symbol_list:
            print('invalid symbol')
        
        print(f'{x} {symbol} {y} = {result}')
        print(f'type "yes" to continue calculation with {result}')
        print(f'type "no" to run again all the program')
        exit = input('type "exit" to exit----> ')

        if exit == 'yes'.lower():
            x = result
            for key in operation_dictionary:
                print(key)
        elif exit == 'no'.lower():
            run_again = False
            os.system('clear')
            calculator()
        elif exit == 'exit'.lower():
            run_again = False

calculator()