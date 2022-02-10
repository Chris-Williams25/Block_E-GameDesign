#Chris Williams
#2/9/2022
#My Wordle Game

import os, random
from modulefinder import IMPORT_NAME
os.system('cls') 
word=""
guess=""
def playagain():
    restart=input("Would you like to play again? yes or no?") 
    if restart == 'yes':
        os.system('cls') 
        global GameOn
        GameOn=True
        global tries
        tries=0
        global CountLetter
        CountLetter=0
        menu()
        # SelectWord()
        # GuessFunction() 
    elif restart == 'no':
        GameOn=False
        os.system('cls')
        print("Wow! You got", score, "Points!")
        print("GoodBye!!!")    
    else: 
        print("What? Say that again.") 
        playagain()
def fruits():
    global word
    fruits=["bananas", "grapes", "watermelon", "papaya", "oranges", "tomatoes", "kiwis", "mangos", "apples", "strawberries", "blackberries"]
    word=random.choice(fruits) 
def computerparts():
    global word
    computerparts=["monitor", "microchip", "cpu", "keyboard", "motherboard", "battery", "storage",]
    word=random.choice(computerparts) 
def famousbuildings():
    global word
    famousbuildings=["tajmahal", "eiffeltower", "sydneyoperahouse", "romancolosseum", "towerofpisa", "whitehouse", "spaceneedle", "lourvemuseum"] 
    word=random.choice(famousbuildings) 

def menu():
    print("""
    *******************************
    *_+_+_+_+_+_+_+_+_+_+_+_+_+_+_*
    *     My New Wordle Game      *
    *_+_+_+_+_+_+_+_+_+_+_+_+_+_+_*
    *******************************
    -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    FOR FRUITS SAY 1
    -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    FOR COMPUTER PARTS SAY 2 
    -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    FOR FAMOUS BUILDINGS SAY 3 """)
    User=input("Well, what do you want to play?") 
    if "1" in User:
        fruits()
            # global word
            # fruits=["bananas", "grapes", "watermelon", "papaya", "oranges", "tomatoes", "kiwis", "mangos", "apples", "strawberries", "blackberries"]
            # word=random.choice(fruits) 
    elif "2" in User:
        computerparts()
        # computerparts=["monitor", "microchip", "cpu", "keyboard", "motherboard", "battery", "storage",]
        # word=random.choice(computerparts) 
    elif "3" in User:
        famousbuildings()
        # famousbuildings=["tajmahal", "eiffeltower", "sydneyoperahouse", "romancolosseum", "towerofpisa", "whitehouse", "spaceneedle", "lourvemuseum"] 
        # word=random.choice(famousbuildings) 
    else:
        print("What?")

def GuessFunction(): 
    global guess
    check=True
    while check:
        try:
            guess=input("enter a letter to guess the word: ") 
            if guess.isalpha() and len(guess)==1:
                check=False
            else:
                print("only one letter please") 
                GuessFunction()
        except ValueError:
            print("What? give us another value?") 
            GuessFunction()

GameOn=True
tries=0
score=0
LetterGuessed="" 
menu()
while GameOn:
    GuessFunction() 
    LetterGuessed += guess #This is equal to letterguess plus guess(letterguessed=guess+letterguess) 
    if guess not in word:
        tries +=1
        print(tries) #For testing
    CountLetter=0 
    for letter in word:
        if letter in LetterGuessed:
            print(letter, end=" ") 
            CountLetter +=1 
            score +=1
        else:
            print("_", end=" ")
    if tries >6:
        print("\n Sorry, You've run out of chances") 
        GameOn=False
        playagain() 
    if CountLetter == len(word):
        print("YAY!") 
        GameOn=False
        playagain() 