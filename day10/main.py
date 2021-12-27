from webbrowser import get
from game_data import data
from logos import * 
import random

def get_random_account(data):
    '''Get random account from data list'''
    return random.choice(data)

def showData(account):
    '''lets use this funcion to be to print all my information-'''    
    name = account['name']
    description = account['description']
    country = account['country']

    return f'{name}, a {description}, from {country}' 

def check_answer(guess, a_follwers, b_followers):
    '''Funtion to check fllowera against user;s guess and return
    True if they got it right or false if we got a mistake'''
    if a_follwers > b_followers:
        return guess == 'a'
    elif a_follwers == b_followers:
        return True
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

        while account_a == account_b

