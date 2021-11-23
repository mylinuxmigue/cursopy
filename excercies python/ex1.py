print("Welcome to Treasure island. Your mission is to find the treasure.")

game = input("left or rigth? (l/r)").lower()

if game == "l":
    game = input("swim or wait? (s/w)").lower()
<<<<<<< HEAD
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


=======
    if game == "w":
        game = input("Which door? (Red,Yellow,Blue)").lower()
        if game == "red":
            print("Burned by fire. Game Over.")
        elif game == "yellow":
            print("You win!")
        elif game == "blue":
            print("Eaten by beasts. Game Over.")
        else:
            print("Game Over.")
    else:
        print("Attacked by trout. Game Over.")
else:
    print("Fall into a hole. Game Over.")
>>>>>>> ad7b2ae9f12abbf249b07c8da115e4299fd72c06
