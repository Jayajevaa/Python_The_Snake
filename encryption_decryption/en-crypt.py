from shlex import join
import os

os.system('cls')

menu=int(input("-------------MENU--------------\npress 1 for encryption or decryption\npress 2 to exit\n"))
end=True
while end ==True:

    direction=input("type 'encryt' to encryt and type 'decrypt' to decrypt\n").lower()
    if direction[0]=='e':
        shit='encrypt'
    else:
        shit='decrypt'
    alph =['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    text=input(f"enter the text you want to {shit}\n").lower()
    shift=int(input("enter the shift code\n"))


    def ceaser(text, shift):
        output=""
        if direction[0]=='d':
                shift*= -1
        for letter in text:
            position=alph.index(letter)
            
            new_position=position + shift 
            output += alph[new_position]
        print(f"your {shit}ed code is '{output}'")


    ceaser(text=text,shift=shift)
    end_t=input("do you want to end? (y/n)\n").lower()
    if end_t == 'y':
        end=False

print("thank you for using our app")

