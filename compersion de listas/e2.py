


def vowel_removed(str):
    vowels = ['a','e','i','o','u']

    #first way 
    final_list = []
    for letter in str:
        if letter not in vowels:
            final_list.append(letter)
    return final_list


    #second way 
    #final_list = [letter for letter in str if letter not in vowels]
    #text = ''.join(final_list)

   # return ''.join([letter for letter in str if letter not in vowels])

word = vowel_removed('miguela')
print(word)