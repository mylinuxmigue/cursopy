def find_number (numbers, select):
    for num in numbers:
        if select == num:
            return True
    return False
numbers = [1,2,5]
select = print(input("dame un valor para comparar: "))
print(find_number(numbers,select))



"""numbers = [1,2,5]
select = 2
for num in numbers:
        if select == num:
            print(True)
        else:
            print(False)"""

