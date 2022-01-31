#Chris Williams
#1/27/2022

import os, random
os.system('cls') 


# We need to set up variables
# if the user gives Rock 
#then convert it to 1
#if user gives paper
#then Convert it to 2
#if the user gives scissors
#then convert it to 3
#all as integers
#have the computer choose thier answer before the user.
#userguess=input()
#
#if userguess=computer
#then print (guess again) 
#if userguess is 1 and computer is 

#rock
#paper 
#if computer=1 and userguess=2
#then then user wins
#if computer=2 and userguess=1
#then computers wins
#if userguess=3 computer=1 
#then computer wins
#if computer=3 userguess=1
#then user wins
#if computer=2 userguess=3 
#then computer wins
#if userguess=2 computer=3
#then user wins.
def menu():
    print("********************************")
    print("*+====-=========+=======-=====+*")
    print("*|    Wonderous Rochambeau    |*")
    print("*| Say Your Play in Lower Case|*") 
    print("*+====-=========+=======-=====+*")
    print("********************************")
choosing=True
os.system('cls') 
menu()
while(choosing):
    computer=random.randint(1,3) 
    user=input("What do you want to play? rock, paper, or scissors? ")
    if 'rock' in user:
        user = int(1) 
        choosing=False
        Game=True
    elif 'paper' in user:
        user = int(2) 
        choosing=False
        Game=True
    elif 'scissors' in user:
        user = int(3)
        choosing=False
        Game=True
    else:
        print("What? Say it again.") 
    while(Game):
        if user == 1 and computer == 1:
            print("ROCK!") 
            print("What a coincidence, That's what I got.") 
            Game=False
            Restaring=True
        elif user == 1 and computer == 2:
            print("PAPER!")
            print("You Lost! Try Again!")
            Game=False
            Restaring=True
        elif user == 1 and computer == 3:
            print("SCISSORS!") 
            print("Good job! You Won!")
            Game=False
            Restaring=True
        elif user == 2 and computer == 1:
            print("ROCK!") 
            print("Good job! You Won!")
            Game=False
            Restaring=True
        elif user == 2 and computer == 2:
            print("PAPER!")
            print("What a coincidence, That's what I got.") 
            Game=False
            Restaring=True
        elif user == 2 and computer == 3:
            print("SCISSORS!") 
            print("You Lost! Try Again!")
            Game=False
            Restaring=True
        elif user == 3 and computer == 1:
            print("ROCK!") 
            print("You Lost! Try Again!")
            Game=False
            Restaring=True
        elif user == 3 and computer == 2:
            print("PAPER!")
            print("Good job! You Won!")
            Game=False
            Restaring=True
        elif user == 3 and computer == 3:
            print("SCISSORS!") 
            print("What a coincidence! That's what I got")
            Game=False
            Restaring=True
    while(Restaring): 
        restart=input("Do you want to play agian? ")
        if restart == 'yes':
            os.system('cls')
            menu() 
            choosing=True
            Game=False
            Restaring=False
        elif restart == 'no':
            print(":(") 
            choosing=False 
            Game=False
            Restaring=False
        else:
            print("What? say that again") 
            Restaring=True
            choosing=False 
            Game=False
#Testing




        






    
    
    







# while(Game):
    #     if user == 1 and computer == 2:
    #         print("You Win!!")
    #         choosing=True
    #     elif user == 2 and computer == 1:
    #         print("Nope, Bad Guess") 
    #         choosing=True
    #     elif user == 3 and computer == 1:
    #         print("You Win!!")
    #         choosing=True
    #     elif user == 1 and computer == 3:
    #         print("Nope, Bad Guess") 
    #         choosing=True
    #     elif user == 3 and computer == 2:
    #         print("You Win!!")
    #         choosing=True
    #     elif user == 2 and computer == 3:
    #         print("Nope, Bad Guess") 
    #         choosing=True
    #     elif int(user) ==int(computer):
    #         print("What a Coinsidence! That's what I got!")
    #         choosing=True
    #     Game=False
# user='paper'
# computer=1



# if 'p' in user:
#     user = int(1)
#     print("paper"+str(user)) 
# elif 'ro' in user: 
#     user= int(2)
#     print("rock")
# elif 's' in user:
#     user=int(3) 