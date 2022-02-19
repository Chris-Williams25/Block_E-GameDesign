#Chris Williams
#2/8/2022
#Word game with three levels.
#1-Fruits
#2-Animals
#3-Computer parts
#Choice:

#Create Word Lists.
from modulefinder import IMPORT_NAME
import os, random
fruits=["bananas", "grapes", "watermelon", "papaya", "oranges", "tomatoes", "kiwis", "mangos", "apples", "strawberries", "blackberries"]
# print(len(fruits) this function can tell us the length of a list.
#in python, it doesnt matter if you use "" or ''.
# 
# Now, there are two ways to write the method of showing what object the computer randomly picks
#  
# size= len(fruits) 
# randy= random.randint(0,size) 
# print(randy) 
# word=fruits[randy]
# print(word) 

os.system('cls') 
#this first way is fairly complicated with a 

# word=random.choice(fruits) 

# guess=input("enter a letter to guess the word: ") 
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
        SelectWord()
        # SelectWord()
        # GuessFunction() 
    elif restart == 'no':
        GameOn=False
        os.system('cls') 
    else: 
        print("What? Say that again.") 
        playagain()
def SelectWord():
    global word
    fruits=["bananas", "grapes", "watermelon", "papaya", "oranges", "tomatoes", "kiwis", "mangos", "apples", "strawberries", "blackberries"]
    word=random.choice(fruits) 
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
        except ValueError:
            print("What? give us another value?") 
SelectWord()
GameOn=True
tries=0
LetterGuessed="" 
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


#Now we need to calculate score.
#and have a function for playing the game.