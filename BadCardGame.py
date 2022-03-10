#first let's import random since we will be shuffling
from operator import truediv
import random, os
os.system('cls')
deck=[]
#next, let's start building lists to build the deck
#NumberCards is the list to hold numbers plus face cards
numberCards = []
suits = ["♠","♥","♦","♣"]
royals = ["J", "Q", "K", "A"]
tempplyr1=[]
tempplyr2=[]
#using loops and append to add our content to numberCards :
def TheDeck():
    global royals
    global suits
    global deck
    global numberCards
    global counter
    for i in range(2,11):
        numberCards.append(str(i))
        #this adds numbers 2-10 and converts them to string data

    for j in range(4):
        numberCards.append(royals[j])
        #this will add the card faces to the base list
    #Create full deck
    for k in range(4):   # four suits
        for l in range(13): #13 cards per suit
            card = (numberCards[l] + " " + suits[k])
            #this makes each card, cycling through suits, but first through faces
            deck.append(card)
            #this adds the information to the "full deck" we want to make
    #you can print the deck here, if you want to see how it looks
    print(deck)
    #now let's see the deck!
    counter=0
    for row in range(4):
        for col in range(13):
            # print(deck[counter], end=" ")
            counter +=1
        # print()
#now let's shuffle our deck!
#Shuffle the deck cards
def shuffling():
    global player1
    global player2
    random.shuffle(deck)
    player1=[]
    player2=[]
    # you could print it again here just to see how it shuffle
    #loop to devide the cards to each player
    for l in range(52):
        if l%2==0:
            player1.append(deck[l])
        else:
           player2.append(deck[l])
def splittingthedeck():
    global halfDeck
    global plyr1
    global plyr2
    halfDeck=int(len(deck)/2)
    plyr1=0
    plyr2=0
# print("player1 ",player1)
# print()
# print("player2 ",player2)
Gameon=True
TheDeck()
shuffling()
splittingthedeck()
print(halfDeck)
while(Gameon):
    #ask user to hit a key to release cards
    for i in range (0,halfDeck):
        click=input("Press any key to get cards: ")
        print("Player 1     Player 2")
        print("     "+player1[i]+"      "+player2[i])
        if player1[i]>player2[i]:
            tempplyr1.append(player1[i])
            tempplyr1.append(player2[i]) 
            # player1.pop(i)
            # player2.pop(i)
        elif player1[i]<player2[i]: 
            tempplyr2.append(player1[i])
            tempplyr2.append(player2[i])  
            # player1.pop(i)
            # player2.pop(i)
    print("player one has", len(tempplyr1), "cards in thier deck, player two has", len(tempplyr2), "cards in thier deck")
    print("Round ended")
        # print("Player I: "+str(plyr1)+"     Player II: "+ str(plyr2)
    if (len(tempplyr1))==0:
        Gameon=False
        print("Player two won the game ") #+str(plyr2)+" to "+str(plyr1))
    elif (len(tempplyr2))==0:
        Gameon=False
        print("Player one won the game ") #+str(plyr1)+" to "+str(plyr2))   
    else:
        if len(tempplyr1)<len(tempplyr2):
            halfDeck=len(tempplyr2)
        elif len(tempplyr2)<len(tempplyr1):
            halfDeck=len(tempplyr1)  
        otherone=player1[halfDeck: ]
        othertwo=player2[halfDeck: ]
        if len(player1)>len(player2):
            tempplyr1.extend(otherone) 
        elif len(player2)>len(player1):
            tempplyr2.extend(othertwo) 
        for j in range(0,halfDeck):
            player2.pop(0)
            player1.pop(0) 
        player1.extend(tempplyr1) 
        player2.extend(tempplyr2)
        tempplyr1.clear()
        tempplyr2.clear()

              # else:
    #     if len(player1)>len(player2):
    #         player1.slice(halfDeck) 


    # else:
    #     player1.extend(tempplyr1) 
    #     player2.extend(tempplyr2)


