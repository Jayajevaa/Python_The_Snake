import random
import os
os.system('cls')
letter=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
number=['1','0','2','3','4','5','6','7','8','9']
symbol=['!','@','#','$','%','%','^','&','*']
print('-----WELCOME..TO..PASSWORD..GENERATOR-----')
type=input("do you want\npassword\notp\ncaptcha\n").lower()
if type[0]=='p':
    n_letter=int(input('how many letters would you like to have?\n'))
    n_number=int(input('how many numbers would you like to have?\n'))
    n_symbol=int(input('how many symbols would you like to have?\n'))
elif type[0]=='o':
    n_letter=0
    n_symbol=0
    n_number=6
elif type[0]=='c':
    n_letter=3
    n_symbol=1
    n_number=2


#easy level - medium strenth password
password_1=[]
for char in range(1,n_letter+1):
    password_1.append(random.choice(letter))
for char in range(1,n_number+1):
    password_1.append(random.choice(number))
for char in range(1,n_symbol+1):
    password_1.append(random.choice(symbol))
os.system('cls')
print("--------------------------------\n \n \n")

random.shuffle(password_1)
pass_str=''
for i in password_1:
    pass_str += i
name=''
if type[0]=='p':
    name='password'
elif type[0]=='o':
    name='otp'
elif type[0]=='c':
    name='captcha'

print(f'{name} : {pass_str} \n\n\n\n--------------------------------')

