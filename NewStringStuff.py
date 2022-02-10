# #Chris WIlliams
# #1.31.2022
# #strings are an array of characters.

# #it has many functions
import os, random
from xml.etree.ElementTree import TreeBuilder
os.system('cls') 


# myName= 'Chris Williams' 
# #so C is 0, H is 2, R is 3 and so on. 
# #This is an array
# myStatement=""" My Name is so nice becuase blah blah blaj

# Whatever
# ever"""

check=True
while(check):
    letter=input("Dear User, please give us a nice letter: ") 
    if len(letter)>1 or not letter.isalpha(): #alpha as in the alphabet. the condition sets it to only accept charachters from the alphabet.
        print("Bad") 
        check=True
        Game=False
    else:
        check=False
        Game=True

while(Game): 
    words=["radio", "clues", "suite", "peter", "robot"] 
    word=random.choice(words)
    print(word)
    for i in range(len(word)): 
        if letter == word[i]:
            print(letter, end= " ")
        else:
            print("_", end=" ")
        Game=False
        Check


# for elem in myStatement:
#     print(elem, end=" ") 
# guess=random.choice(myName) 
# print(guess) 