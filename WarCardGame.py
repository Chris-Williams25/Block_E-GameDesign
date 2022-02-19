import os, random
os.system('cls')
# numberCards=[]
# for i in range(2,10):
#     numberCards.append(i)
#     numberCards[i-2]=str(numberCards[i-2]) 
#     print(numberCards) 
#     suits=("♠,♥,♦,♣")
#     royals=("K","J","Q","A")
#     #make a list like this (2,3,4,5,6,7,8,9,10,11,J,Q,K,A) 
#     #create a deck of cards adding each suit
#     cards=("2","3","4","5","6","7","8","9","10")
royals=['K','K','K','K','Q','Q','Q','Q','J','J','J','J','A','A','A','A']
heartsuits=['♥2','♥3','♥4','♥5','♥6','♥7','♥8','♥9','♥10'] 
spadesuits=['♠2','♠3','♠4','♠5','♠6','♠7','♠8','♠9','♠10']
diamondsuits=['♦2','♦3','♦4','♦5','♦6','♦7','♦8','♦9','♦10']
clubssuits=['♣2','♣3','♣4','♣5','♣6','♣7','♣8','♣9','♣10']
Cards=[]
# Cards.extend(royals and heartsuits and spadesuits and diamondsuits and clubssuits) #This way does not work
Cards.extend(heartsuits)
Cards.extend(royals)
Cards.extend(spadesuits)
Cards.extend(diamondsuits)
Cards.extend(clubssuits) 
size=len(Cards)
print(Cards)
print("There is", +size, "cards in this deck.") 
randomCard=random.choice(Cards)
print(randomCard)
# print("Here's a random card", +randomCard) #why doesn't this work
