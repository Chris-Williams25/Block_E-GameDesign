import random

suits = ['Hearts','Clubs','Spades','Diamonds']

ranks = ['Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Jack','Queen','King','Ace']

values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six' : 6 , 'Seven' :7, 'Eight': 8,'Nine':9,
          'Ten':10,'Jack':11, 'Queen': 12,'King': 13,'Ace':14 }
class Card():  
    
    
    def __init__(self,suit,rank):
        
        self.suit = suit
        self.rank = rank
        self.value = values[rank]
    
    #string method
    def __str__(self):
        
        return self.rank + ' of ' + self.suit 

class Deck():

  def __init__(self):

    self.all_cards = []  #list of objects

    for suit in suits:

      for rank in ranks:
        #create card object

        created_card = Card(suit,rank)

        self.all_cards.append(created_card)


  def shuffle(self):   #method to shuffle the card

    random.shuffle(self.all_cards)



  def deal_one(self):

    return self.all_cards.pop()  #we want the last card from deck


class Player():

  def __init__(self,name):

    self.name  = name
    self.all_cards = []

  def remove_one(self):

    return self.all_cards.pop(0)    #to remove card from beginning of the list

    

  def add_cards(self,new_cards):


    if type(new_cards) == type([]):

      self.all_cards.extend(new_cards)

    else:

      self.all_cards.append(new_cards)

  def __str__(self):
    return f'Player {self.name} has {len(self.all_cards)} cards.'
    

  def deal_one(self):

    return self.all_cards.pop()  #we want the last card from deck


class Player():

  def __init__(self,name):

    self.name  = name
    self.all_cards = []

  def remove_one(self):

    return self.all_cards.pop(0)    #to remove card from beginning of the list

    

  def add_cards(self,new_cards):


    if type(new_cards) == type([]):

      self.all_cards.extend(new_cards)

    else:

      self.all_cards.append(new_cards)

  def __str__(self):
    return f'Player {self.name} has {len(self.all_cards)} cards.'
    
# And below is the final game logic:

#create 2 new instances of the player class

player1_name = input('Enter the name of Player1: ')

player2_name = input('Enter the name of Player2: ')

player1 = Player(player1_name)
player2 = Player(player2_name)
newdeck = Deck()
newdeck.shuffle()

#splitting the deck among the two players - alternate card from deck goes to each player respectively

for i in range(0,len(newdeck.all_cards)-1,2):  

  player1.add_cards(newdeck.all_cards[i])
  player2.add_cards(newdeck.all_cards[i+1])

#for x in range(26):

 # player1.add_cards(newdeck.deal_one())
  #player2.add_cards(newdeck.deal_one())

print(player1)
print(player2)


game_status = True
    
round_num = 0
while game_status == True:

  round_num +=1
  print(f"Round {round_num}")


  if len(player1.all_cards) == 0:

    print('Player 1 out of cards'+ player2.name + 'Wins!')
    game_status = False
    break
  
  if len(player2.all_cards) == 0:

    print('Player 2 out of cards' + player1.name + 'Wins!')
    game_status = False
    break


  else:

     
    player_cards = []
    player1_card = player1.remove_one()
    player2_card = player2.remove_one()
    player_cards.append(player1_card)
    player_cards.append(player2_card)
    
    

    print('player1_card_value: ',player1_card.value)
    print('')
    print('player2_card_value: ',player2_card.value)
    print('')
    print(player1)
    print('')
    print(player2)


    at_war = True

    

    if player1_card.value == player2_card.value:  

      while at_war == True:


        player1_list = []
        player2_list = []

        card_list = []


        if len(player1.all_cards) < 5:
            
          print('Player 2 won')

          game_status = False
          at_war = False
          
          break

        elif len(player2.all_cards) <5:

          print('Player 1 won')
          game_status = False
          at_war = False
          break

        if len(player1.all_cards) >= 5 and len(player2.all_cards) >= 5:

          for i in range(5):
            player1_list.append(player1.remove_one())
            player2_list.append(player2.remove_one())


          card_list.extend(player1_list)
          card_list.extend(player2_list)

          print("CARD LIST LEN", len(card_list))

          if player1_list[0].value > player2_list[0].value:

            player1.add_cards(card_list)
            at_war = False
            break


          elif player1_list[0].value < player2_list[0].value:

            player2.add_cards(card_list)
          #player2.add_cards(player1_list)
            at_war = False
            break

          else:

            at_war = True

      


    elif player1_card.value > player2_card.value:

      player1.add_cards(player_cards)
      #player1.add_cards(player2_cards)

      #print('p1>p2', player1)

    elif player2_card.value > player1_card.value:

      player2.add_cards(player_cards)
      

    
          
        
            

     
print(player1)
print(player2)

if len(player1.all_cards) == 0:
  print('Player 2 won')

elif len(player2.all_cards) == 0:
  print('Player 1 won')