#Chris Williams
#1/26/2022

import os 
os.system('cls') 
import os, random
check=True
def menu():
    print("     =-+-=-+-=-+-=-+-=-+-=-+-=")
    print("     |   WELCOME TO THE      |")
    print("     |  GREATEST GAME EVER   |")
    print("     =-+-=-+-=-+-=-+-=-+-=-+-=")
    print(' {-= FOR GAMEMODE ONE PRESS "1" =-}')
    print(' {-= FOR GAMEMODE TWO PRESS "2" =-}')
    print('{-= FOR GAMEMODE THREE PRESS "3" =-}')
    print("Gamemode one is 10 numbers and five attempts")
    print("Gamemode two is 15 numbers and seven attempts")
    print("Gamemode three is 20 numbers and ten attempts") 

RunGame=True
while (RunGame):
    menu() #This is calling the function "Menu"
    #Checking for correct user input
    while check:
        try: 
            choice=int(input("Choice: "))
            if choice>0 and choice<4:
                check=False
            else:
                print("Sorry, Wrong Choice. Please enter 1-3") 
        except ValueError:
            print("Sorry, Wrong Choice. Please enter 1-3") 

    if choice ==1:
        MyNumber= random.randint(1, 10) 
        attempts=5
    elif choice ==2:
        MyNumber= random.randint(1, 15)
        attempts=7
    elif choice ==3:
        MyNumber= random.randint(1, 20) 
        attempts=10
    print(choice)
    GameOn=True
    while(GameOn):
        userGuess=(input("Give me a Number: "))
        if str(userGuess) == "quit":
            os.system('cls')
            GameOn=False
        else:
            userGuess = int(userGuess)
        if MyNumber == userGuess:
            print("You Guessed It!")
            GameOn=False
        else:
            print('Incorrect!')
            attempts=attempts-1
            print("You have", attempts, "attempts left") 
        if int(attempts) ==0:
            RunGame=False
            print("You've failed")
            restart=input('Do you want to play again?')
            GameOn=False
    print("The Number to guess was "+str(MyNumber)) 
    if restart == 'yes':
        os.system('cls')
        menu()
        RunGame=True
        check=True
    else:
        print("What? yes? Okay whatever you say! Play again!")
        menu()
        RunGame=True
        check=True
    


#I have to make it so if one were to want to play, if you say yes, It opens the menu.

# if str.isnumeric(userGuess):

# print("=-+-=-+-=-+-=-+-=-+-=-+-=")
# print("|   WELCOME TO THE      |")
# print("|  GREATEST GAME EVER   |")
# print("=-+-=-+-=-+-=-+-=-+-=-+-=")
# print('{-= FOR GAMEMODE ONE PRESS "1" =-}')
# print('{-= FOR GAMEMODE TWO PRESS "2" =-}')
# print('{-= FOR GAMEMODE THREE PRESS "3" =-}')

