import random
import os
import time

os.system('cls')
print("hello welcome to number guessing game")
time.sleep(2)
os.system('cls')
print("choose your difficulty level.....\n")
time.sleep(1)
print("easy------ 1")
time.sleep(1)
print("medium---- 2")
time.sleep(1)
print("hard------ 3")
time.sleep(1)
print("asian----- 4")

ran=100

menu=input()
if menu == '1':
    num=10
elif menu == '2':
    num= 7
elif menu== '4':
    num=5
    ran=200
else:
    num=5

os.system('cls')

computer_guess = random.randint(0,ran)
print("i am thinking of a number.............")

time.sleep(2)

os.system('cls')

print(f"i have guessed a nummber between 0 to {ran}")
time.sleep(1.5)
won=0
for i in range(0,num):
    os.system('cls')
    print(f"you have {num-i} guesses left")
    user_guess=int(input("guess a number\n\n"))
    if user_guess > computer_guess:
        print("too high")
        time.sleep(2)
    elif user_guess< computer_guess:
        print("too low")
        time.sleep(2)
    else:
        print("you got the number")
        time.sleep(2)
        won = 1
        os.system('cls')
        break
    
if won == 1:
    print("\n\n\nYOU WON\n\n\n")
else:
    print("\n\n\nYOU LOST\n\n\n")
    print(computer_guess)
