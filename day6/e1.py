"""def sum(x,y):
    return x + y
print(sum(2.3))
print(sum(-2,10))"""

from operator import truediv


def max(a,b):
    return a > b
    """if a > b:
        return True
    else: 
        return False"""

print(type(max(2,5)))



x = int(input("type a number: "))
y= int(input("type another number: "))
if max(x,y):
    print("first number is bigger than second")
elif not max(x,y):
    print("second number is bigger tha first")

