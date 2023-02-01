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


    for j in range(4):
        numberCards.append(royals[j])

    for k in range(4): 
        for l in range(13):
            card = (numberCards[l] + " " + suits[k])
            deck.append(card)

    print(deck)

    counter=0
    for row in range(4):
        for col in range(13):
            # print(deck[counter], end=" ")
            counter +=1
TheDeck()
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
shuffling()
halfDeck=int((len(deck)/2))
print(player1)
print(player2)
Gameon=True
while Gameon:
    for i in range(0,halfDeck):
        print("Player 1     Player 2")
        print("     "+str(player1[i])+"      "+str(player2[i]))