import random #importing the random module
import hangman_art #importing nessasary files
import hangman_words #importing nessasary files
import os #used to clear screen or terminal after each entry using os.system('cls')

os.system('cls')


print(f"\n\n{hangman_art.logo}")

print("\n\nNEW GAME PRESS 1\nREAD RULES PRESS 2\nEXIT GAME PRESS 3")
game=int(input(""))

score=0
if game==1 or game==2:
    

    if game==2:
        os.system('cls')
        print(hangman_words.rules)
    else:
        os.system('cls')
    for j in range(0,3,1):
        print(f"ROUND {j+1}\n\nscore :{score}")

        print("\nchoose your level of difficulty :\nfruits press 1\nanimals press 2\nasian level press 3\nwant us to make even better levels press 4\n")
        level=int(input(""))
        if level == 1 or level==2 or level==3:
            if level==1:
                word_list=hangman_words.fruits
            elif level==2:
                word_list=hangman_words.fruits
            else:
                word_list=hangman_words.shit



            word=random.choice(word_list)




            word_len=len(word)


            display=[]
            for letter in word:
                display+='_'


            end_of_game=False
            lifes=6

            os.system('cls')
            while not end_of_game:

                guess=input('\nguess a letter and enter :\n'+f"{' '.join(display)}\n"+hangman_art.stages[lifes]+"\n\n").lower()

                if guess in display:
                    os.system('cls')
                    print(f"{' '.join(display)}")
                    print(f"\nyou have already guessed '{guess}' ")
                    lo=input("press enter to keep playing")


                for i in range(0,word_len):
                    if word[i]== guess:
                        display[i]=word[i]
                    
                    
                print(f"{' '.join(display)}") #join the elements in the list togather
                
                if '_' not in display:
                    end_of_game=True
                    
                    os.system('cls')
                    print(f"\nThe word is : {word}")
                    score+=1
                    print(f"\n\n\n{hangman_art.win}\n\n\n")
                    lo=input(f"press enter to go to round {j+2}")
                    os.system('cls')
                    break
                
                
                if guess not in word:
                    lifes-=1
                
                    
                
                print(hangman_art.stages[lifes])
                os.system("cls")
                if lifes==0:
                    os.system('cls')
                    print(f"\n\n{hangman_art.stages[lifes]}")
                    print(f"\nThe correct word is : {word}")
                    print(f'\n\n{hangman_art.lose}\n\n\n')
                    
                    end_of_game=True
                    lo=input(f"press enter to go to round {j+2}")
                    os.system('cls')

                    break
                
        
            print(f"\n\nyour final score: {score}\n\n")         
        else:        
            os.system('cls')
            print("the level entered is not available\n\nbut will be taken into consideration and added in the next update\n\nplease specify the list name you would like to have\n")
            sugg=input("")
            file=open('hangman_suggestion.txt','a')
            file.write(f"{sugg}\n")
       

else:
    os.system('cls')
    print("thank you for playing the game\nsee ya")