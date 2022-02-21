from game_data import data
from logos import *
import random
import os

def  get_random_account(data):
    '''Get random account from data list'''
    return random.choice(data)

def showdata(account):
    '''Lets use this funtion to be to print all my information'''
    name = account['name']
    description = account['description']
    country = account['country']
    return f'{name} a {description} from {country}' 

def check_answer(guess,a_followers,b_followers):
    '''funtion to check followers against user's guess and return 
    True if they got it rigth or false if we gota mistake'''
    if a_followers > b_followers:
        return guess == 'a'
    else:
        return guess == 'b'

def game():
    print(logo)

    game_should_continue = True
    account_a = get_random_account(data)
    account_b = get_random_account(data)

    while game_should_continue:
        account_a = account_b
        account_b = get_random_account(data)
        score = 0

        while account_a == account_b:
            account_b = get_random_account(data)

        print(f'compare A: {showdata(account_a)}')
        print('vs')
        print(f'compare B {showdata(account_b)}')

        guess =input('Who has more followers? Type "A" or "B": ').lower()
        
        #lets validate followers
        a_followers = account_a['follower_count']
        b_followers = account_b['follower_count']
        result = check_answer(guess,a_followers,b_followers)
        os.system('clear')
        #if result == True, that meansyou were rigth
        #lets modify the score value

        if result:
            score = score + 1
            print(f'you were right! your current score is {score}')
        elif not result:
            game_should_continue = False
            print(f'Sorry, thats wrong. Final score {score}')

game()