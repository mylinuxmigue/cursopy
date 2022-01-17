import random


stages = ['''
   +---+
   |   |
   O   |
  /|\  |
  / \  |
        |
  =========
  ''', '''
   +---+
   |   |
   O   |
  /|\  |
  /    |
        |
  =========
  ''', '''
   +---+
   |   |
   O   |
  /|\  |
        |
        |
  =========
  ''', '''
   +---+
   |   |
   O   |
  /|   |
        |
        |
  =========''', '''
    +---+
    |   |
    O   |
    |   |
        |
        |
  =========
  ''', '''
    +---+
    |   |
    O   |
        |
        |
        |
  =========
  ''', '''
    +---+
    |   |
        |
        |
        |
        |
  =========
  ''']

def random_chosen_word():
      word_list = ['hangman', 'hanna', 'computer', 'python','airplane','spiderman']
      return random.choice((word_list))

def create_display(chosen_word):
      display = []
      for char in range(len(chosen_word)):
            display.append('_')
      return display

def check_character(chosen_word,display,guess):
      end_of_game = True
      lives = 6

      while end_of_game:
            guess = input('Guess a letter: ').lower()

            for position in range(len(chosen_word)):
                  letter = chosen_word[position]

                  if letter == guess:
                        display[position] = letter
            
            if guess not in chosen_word:
                  lives -=1
                  print(stages[lives])
                  print(f'your have {lives} lives')
                  if lives == 0:
                        end_of_game =False
                        print('you lose')
            print(display)

            if '_' not in display:
                  end_of_game = False
                  print('you win')
                  final_word = ''
                  for element in display:
                        final_word += element
                  print(f'secret word was {final_word}')
                  
            

choisen_word = random_chosen_word()
#print(choisen_word)
display_out_funtion = create_display(choisen_word)
print(display_out_funtion)
check_character(choisen_word,display_out_funtion,stages)






chosen = random_chosen_word()
print(chosen)
print(create_display(chosen))
