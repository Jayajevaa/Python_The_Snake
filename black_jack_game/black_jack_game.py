import random
import os
os.system('cls')

def deal_card():
    '''randomly deals a card from the deck'''
    cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]
    card=random.choice(cards)
    return card

def compare(user_score,computer_score,user_card,computer_card):
    os.system('cls')
    print(f"your cards : {user_card}\nyour oponents cards : {computer_card}")
    if user_score==computer_score:
        return 'DRAW😐'
    elif computer_score ==0: 
        return 'YOU LOST☹️ the opponent had a black jack'   
    elif user_score == 0:
        return 'YOU WON with a black jack😎'
    elif computer_score >21:
        return 'computer had a bad day'
    elif user_score >21:
        return 'its a bad day for u, YOU LOST'
    elif user_score > computer_score:
        return 'YOU WON you had more value that ur opponent'
    else:
        return 'YOU LOST computer got lucky'

def play_game():
    user_card=[]
    computer_card=[]
    game_is_on=True


    for _ in range(2):
        user_card.append(deal_card())
        computer_card.append(deal_card())

    while game_is_on:
        
        def calculate_score(cards):
            '''checks for the nessasary conditions and returns either 0 if user gets 21 and only has 2 cards else it returns sum of the cards or if the sum of the cards are more than 21 it replaces 11 with 1'''
            if sum(cards)==21 and len(cards)==2:
                return 0
            
            if 11 in cards and sum(cards)>21 :
                cards.remove(11)
                cards.append(1)
            return sum(cards)


        user_score=calculate_score(user_card)
        computer_score=calculate_score(computer_card)


        print(f"your cards : {user_card}, current_score : {user_score}")
        print(f"comuters first card : {computer_card[0]}")


        if user_score == 0 or computer_score == 0 or user_score > 21:
            game_is_on=False
        else:
            user_wants_more=input("if you want to deal another card type 'y' and type 'n' to pass :\n").lower()
            if user_wants_more =='y':
                os.system('cls')
                user_card.append(deal_card())
            else:
                game_is_on=False

    while computer_score != 0 and computer_score < 17:
        computer_card.append(deal_card())
        computer_score=calculate_score(computer_card)

    user_score=calculate_score(user_card)
    print(compare(user_score,computer_score,user_card,computer_card))

while input("do you want to play the game ? 'y' or 'n'").lower()=='y' :
    os.system('cls')
    play_game()




