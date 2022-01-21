#Chris Williams
#1/21/2022 

import os
os.system('cls')

#to use random numbers, you have to import random numbers.
#when something is brighter it has been used, when it is dull, it has not been used.
import os, random
# We are going to learn the imput() function,...
# type casting, branching, and (maybe) looping.

# declare variable for user imput 

# print("Enter a number 1-10", end=": ")
# userInfo=int(input())
# print("The number is %.2f " %(userInfo/3))
# guess=int(input("please give me a number"))

#if you want to find the answer as a whole number, you use "%d", but if you want it to the decimal,...
#you use "%.2"

# MyNumber = 9
# UserGuess=int(input("Guess a Nymber from 1-10"))
# if MyNumber ==UserGuess
#     print("You Guessed it!")
# else:
#     print("Not Right!")
# #You need to have two = signs, otherwise the computer thinks the number has to be equal to the wording of the...
# #variable

myNumber=random.randint(1,10)
userGuess=int(input("Guess a nymber from 1-10"))
if myNumber ==userGuess:
    print("You Guessed It!")
else:
    print("Better Luck Next Time!")
#to say the number:
print("The Number was "+ str(myNumber))

