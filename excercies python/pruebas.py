'''dictionary_operations = {'+':'sum',
                         '-':'subtract',
                         '*':'multiplication',
                         '/':'division'}

for _ in dictionary_operations:
    print(dictionary_operations[_])
'''

"""result = "hola"
for a in result:
    print(a)"""

"""def find(list_,num_):
    for num in list_:  
        if num == num_:
            return [True,list_.index(num)]
    return False

n = int(input('gave for a number: '))
print(find([1,2,3,4,5],n))"""

'''def check_character(chosen_word,display,guess):
      #if letter is in chosen_word
      end_of_game = True
      lives = 6

      while end_of_game:
        guess = input("Guess a letter: ").lower()
  
        
        for position in range(len(chosen_word)):
            letter = chosen_word[position]

            if letter == guess:
                display[position] = letter

        if guess not in chosen_word:
            lives -= 1
            print(stages[lives])
            print(f"You have {lives} lives")
            if lives == 0:
                end_of_game = False
                print("You lose")
        print(display)

        if "_" not in display:
            end_of_game = False
            print("You win")
            final_word = ''
            for element in display:
                final_word += element
            print(f"Secret word was  {final_word}")

choisen_word = random_choice_word()
#print(choisen_word)
display_out_function = create_display(choisen_word)
print(display_out_function)
check_character(choisen_word,display_out_function,stages)'''



'''dictionary[] = 
#forma de agregar en diccionarios, palabras claves y su definicion 
dictionary[] = 

#forma de  quitar una palabra clave
dictionary.pop('superman')'''

'''dictionary = {'superman':{'power 1':'he can fly','power 2':'he is strong'},
'flash':'its very fastest man over the world',
'green lanter':'he is the chosen one'}

for key in dictionary:
    print(key)
    print(dictionary[key])'''

'''c0 = int(input('cualquier numero entero positivo: '))
c1 = 0
list = (f'')
while c0 != 1:
    if c0 % 2 == 0:
        c0 = c0/2
    else:
        c0 = 3 * c0 +1 
    list =+ c0
    print(list)
    c1+=1
    print(f'pruebas ={c1}')
'''

numbers = [1,2,3,4,5,6]
for num in range(len(numbers)-1,10):
    print(num)




