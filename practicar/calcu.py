import os
#import time
from log_cal import calcu

def sum(x,y):
    return x+y
def substrac(x,y):
    return x-y
def multiplication(x,y):
    return x*y
def division(x,y):
    return x/y

print(calcu)



def calculator():
    dictionary_calculator = {'+':sum,
                         '-':substrac,
                         '*':multiplication,
                         '/':division}
    x = int(input("type the first value: "))
    for key in dictionary_calculator:
        print(key)

    run_again = True

    while run_again:
        symbol = input('type the operations: ')
        y = int(input('type the second value: '))
        
        calculator_operation = dictionary_calculator[symbol]
        result = calculator_operation(x,y)
        print(f'{x} {symbol} {y} = {result}')
        
        print(f'type yes to continue with the same result {result}')
        print('type no to recalculate ')
        run_continue = input('type any other key to exit ')

        if run_continue == 'yes'.lower():
            x = result
        elif run_continue == 'no'.lower():
            run_again = False    
            os.system('clear')
            #time.sleep(5)
            calculator()
        else:
            run_again = False


calculator()    
