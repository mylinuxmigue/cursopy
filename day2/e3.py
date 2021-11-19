from re import T


heigth = int(input("What is height in cm?"))

can_ride = False

if heigth >= 120:
    can_ride = True
    #age < 12 --- $5
    #age <= 18 --- $7
    #age <= 45 --- $9
    #free

if can_ride:
    age = int(input("How old are you?: "))
    ticket = 0
    if age < 12:
        #ticket = ticket + 5
        ticket += 5
    elif age <= 18: 
        ticket +=7
    elif age <= 45:
        ticket += 9
    #photo = input("Do you want a photo?: (y/n)").lower()
    if input("Do you want a photo?: (y/n)").lower() == "y":
        ticket +=3
    print(f"you have to pay {ticket}")
elif not can_ride:
    print("You cannot ride")

 