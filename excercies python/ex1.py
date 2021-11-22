print("Welcome to treasure island your mission is to find the trasure.")

game = input("left or rigth? (l/r)").lower()

if game == "l":
    game = input("swim or wait? (s/w)").lower()
    if  game == "w":
        game = (input("whitch door? (blue, red, yellow)")).lower()
        if game == "blue":
            print("Eaten by beasts.")
        elif game == "yellow":
            print("you win")
        elif game == "red":
            print("Burned by fire")
        else:
            print("GAME OVER")
    else: 
        print("Attacked by trout")
else:
    print("Fall into a hole") 


