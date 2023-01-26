import random
mylist=['hi','hola','wassup','whaspoppin',"how's it goin?"]
#my list of greetings
def startconvo(name):
    print(mylist[random.randint(0,4)])
    response=input('your response: ')
    while(len(name) > 0):
        if (len(name)%2 == 0):
            print('thanks')
        else:
            print('ight')
        print(mylist[random.randint(0,4)])
        response = input('your response: ')
print("welcome to the friendshipper")
startconvo(input("what's your name?: "))
#based off of Mr. Meagher's class code
#