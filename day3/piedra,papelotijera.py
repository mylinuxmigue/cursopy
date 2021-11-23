import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

list = [rock,paper,scissors]

choice = int(input("Make a choice 0-rock, 1-paper, 2-scissors"))
computer = random.randint(0,2)

if choice == 0 and computer == 2:
    print("you win")
elif computer == 0 and choice == 2:
    print("you lose")
if choice > computer:
    print("User win")
elif choice < computer:
    print("Computer win")
elif choice == computer:
    print("it is a tie") #es empate


print("User:")
print(list[choice])
print("computer")
print(list[computer])
