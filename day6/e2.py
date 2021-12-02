"""def factorial_(n):
    factorial_ = 1
     
    while n>= 1:
        n=-1
    return factorial_

print(factorial_(6))
"""

def factorial(n):
    if n==0 or n == 1:
        return 1 
    elif n>1:
        return n * factorial(n-1)
print(factorial(6))