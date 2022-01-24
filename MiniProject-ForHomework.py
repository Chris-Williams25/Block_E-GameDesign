import os
import os, random
os.system('cls')
print(" ______________\n|Welcome to The|\n|  Game        |\n ==============")
print("\nPick your gamemode\npress 1 for GM1\npress 2 for GM2\npress 3 for GM3")
print("Number", end=": ")

UserInfo=input()
GM1=1 
GM2=2
GM3=3

MyNumber1=random.randint(1,10) 
MyNumber2=random.randint(1,50)
MyNumber3=random.randint(1,100)


#This is a failed system that I thought worked, But it turns out it doesn't.
# if int(UserInfo) ==GM1:
#     ThisGameMode2=False
#     ThisGameMode1=True
#     ThisGameMode3=False
# while(ThisGameMode1):
#     userGuess=int(input("Guess A Number from 1-10: "))
#     if MyNumber1== userGuess:
#         print("\nCongradulations! You got it!" )
#         ThisGameMode1=False
#     else:
#         print("\nNope! Good luck Next Time!")
# print("The Number to guess was "+ str(MyNumber1))

# if int(UserInfo) ==GM2:
#     ThisGameMode2=True
#     ThisGameMode1=False
#     ThisGameMode3=False
# while(ThisGameMode2):
#     userGuess=int(input("Guess A Number from 1-50: "))
#     if MyNumber2== userGuess:
#         print("\nCongradulations! You got it!" )
#         ThisGameMode2=False
#     else:
#         print("\nNope! Good luck Next Time!")
# print("The Number to guess was "+ str(MyNumber2))

# if int(UserInfo) ==GM3:
#     ThisGameMode2=False
#     ThisGameMode1=False
#     ThisGameMode3=True
# while(ThisGameMode3):
#     userGuess=int(input("Guess A Number from 1-100: "))
#     if MyNumber1== userGuess:
#         print("\nCongradulations! You got it!" )
#         ThisGameMode3=False
#     else:
#         print("\nNope! Good luck Next Time!")
# print("The Number to guess was "+ str(MyNumber3))



if int(UserInfo) ==GM1:
    ThisGameMode2=False
    ThisGameMode1=True
    ThisGameMode3=False
if int(UserInfo) ==GM2:
    ThisGameMode2=True
    ThisGameMode1=False
    ThisGameMode3=False
if int(UserInfo) ==GM3:
    ThisGameMode2=False
    ThisGameMode1=False
    ThisGameMode3=True

while(ThisGameMode1):
    userGuess=int(input("Guess A Number from 1-10: "))
    if MyNumber1== userGuess:
        print("\nCongradulations! You got it!" )
        ThisGameMode1=False
        print("The Number to guess was "+ str(MyNumber1))
    else:
        print("\nNope! Good luck Next Time!")


while(ThisGameMode2):
    userGuess=int(input("Guess A Number from 1-50: "))
    if MyNumber2== userGuess:
        print("\nCongradulations! You got it!" )
        ThisGameMode2=False
        print("The Number to guess was "+ str(MyNumber2))
    else:
        print("\nNope! Good luck Next Time!")


while(ThisGameMode3):
    userGuess=int(input("Guess A Number from 1-100: "))
    if MyNumber1== userGuess:
        print("\nCongradulations! You got it!" )
        ThisGameMode3=False
        print("The Number to guess was "+ str(MyNumber3))
    else:
        print("\nNope! Good luck Next Time!")
