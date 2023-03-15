from art import logo,vs
from game_data import data
import random
import os
import time

os.system('cls')


def get_random_account():
    return random.choice(data)

def format_data(account):
    '''takes the account data and returns it in the printable format'''
    account_name=account['name']
    account_description=account["description"]
    account_country=account["country"]

    return(f"{account_name} a {account_description} from {account_country}")

def check_answer(guess,a_foll,b_foll):
    '''checks if the user guess is correct or not'''
    if a_foll>b_foll:
        return guess == 'A'
    else:
        return guess =='B'

def game():
    os.system('cls')
    game_end=False
    print(logo)
    time.sleep(2)
    score=0
    
    account_b=get_random_account()

    while not game_end:
        account_a=account_b
        account_b=get_random_account()

        while account_a == account_b:
            account_b=get_random_account()


        print(f"compare A : {format_data(account_a)}\n{vs}\ncompare B : {format_data(account_b)}\n")

        guess=input("guess who has more followers ? 'A' or 'B'\n").upper()

        a_follower_count=account_a["follower_count"]
        b_follower_count=account_b["follower_count"]

        is_correct=check_answer(guess,a_follower_count,b_follower_count)

        os.system('cls')
        print(logo)
        
        if is_correct:
            score+=1
            print(f" you are right\ncorrect score: {score}")
            
        else:
            print(f"\nsorry, you had a bad guess\nfinal score: {score}\n\n\n")
            game_end=True

game()