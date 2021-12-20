import os
from logo_cal import calcu

def sum(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiplication(a,b):
    return a*b
def division(a,b):
    return a/b

def calculator():
    print(calcu)
    dictionary_operations = {'+':sum,
                            '-':subtract,
                            '*':multiplication,
                            '/':division}
    a = int(input('escribe un numero: '))
    for key in dictionary_operations:
        print(key)
    
    run_again = True

    while run_again:
        symbol = input('selecciona la operacion para el diccionario: ')
        b = int(input('escribe otro: '))

        calculation_function = dictionary_operations[symbol]
        result = calculation_function(a,b)
        print(f'{a} {symbol} {b} = {result}')

        print(f'digita si para continuar calculando con el: {result}')
        print('digita no para correr el programa de nuevo')
        correr_de_nuevo = input('digite exit para salir')
        
        if correr_de_nuevo == 'si'.lower():
            a = result
        elif correr_de_nuevo == 'no'.lower():
            run_again = False
            os.system('clear')
            calculator()
        else:
            run_again = False
calculator()
