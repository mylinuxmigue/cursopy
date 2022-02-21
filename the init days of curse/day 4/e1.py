"""i = 0
while i <= 10:
    print(i)
    i+=1
"""


"""i = 0
list = [1,2,3,4,5,6,7,True]
while i < len(list):
    print(list[i])
    i+=1"""



from itertools import count


"""count = 0
while input("type a message ").lower() != "stop":
    print(count)
    count +=1
"""

   

"""list = []
i = 0
while i <= 10:
    list.append(i)
    i += 1
    print(list) """

"""list = []
i = 0

another_number = True

while another_number == True:
    answer = input("do you want another number? ").lower()
    if answer == "stop":
        another_number = False
    elif answer == "yes" :
        list.append(i)
        i += 1
        print(list) 
    elif answer == "two":
        list.extend([i,i+1])
        print(list)
        i += 1
    else:
        print("it isnot defined")
        another_number = False
"""

list = [[1,2,3],[4,5,6],[7,8,9]]
print(list[0][0])
