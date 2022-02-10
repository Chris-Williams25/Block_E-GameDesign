#Chris WIlliams
#1.31.2022
#strings are an array of characters.

#it has many functions
import os, random
os.system('cls') 


myName= 'Chris Williams' 
#so C is 0, H is 2, R is 3 and so on. 
#This is an array
myStatement=""" My Name is so nice becuase blah blah blaj

Whatever
ever"""

for elem in myStatement:
    print(elem, end=" ") 
guess=random.choice(myName) 
print(guess) 
words=["Radio", "Clues", "suite", "peter", "Robot"] 
word=random.choice(words)
print(word)


print(myStatement) 
print(myName[6])
#If I were to print "[5]"", It would use the space instead of the W. 
#The Numbers begin at 0. 
if 'blah' in myStatement:
    print("True") 
print("expert" not in myStatement) 
#find() will return the index of the character you are looking for (first instance) 
INDEX= myName.find("a")
print(INDEX) 
#finding the length of your word. 
wordLen=len(myName) 
print(wordLen) #your last index is len-1 
print(myName[2]) 
#while loops -> work under a condition (as in Game=True \nwhile(Game))
#"for loops" -> do something for a set few amount of times. 
for i in range(wordLen-1):
    if "a" in myName[1]:
        print(i, end=": ")
print("") 
print("Done") 


myStatement=myStatement.lower() 
print(myStatement) 

check=True
while(check):
    letter=input("Dear User, please give us a nice letter: ") 
    if len(letter)>1 or not letter.isalpha(): #alpha as in the alphabet. the condition sets it to only accept charachters from the alpha 
        print("Bad") 
        check=True
    else:
        check=False
print("ready to play")
# "i" is the counter, it controls the array. 
#we don't need to declare what "i" is in this case
# if letter in myStatement:
#     print("GREAT!!1!!!1") 
# else:
#     print("Bruh wut?")