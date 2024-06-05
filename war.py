import pdb
import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':14}

class Card:
    
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]
        
    def __str__(self):
        return self.rank + ' of ' + self.suit
    
class Deck:
    
    def __init__(self):
        self.all_cards = [] 
        for suit in suits:
            for rank in ranks:
                self.all_cards.append(Card(suit,rank))
                
    def shuffle(self):
        random.shuffle(self.all_cards)
        
    def deal_one(self):
        return self.all_cards.pop()        
    
class Player():
      
    def __init__(self,name):
        self.name=name
        self.my_cards = []
        
    def remove_one(self):
        return self.my_cards.pop(0)
        
    def add_cards(self,new_cards):
        if type(new_cards)==type([]):
            self.my_cards.extend(new_cards)
        else:
            self.my_cards.append(new_cards)
    
    def __str__(self):
        return f"Player {self.name} has {len(self.my_cards)} cards."   
                        
game_on = True
Player_1 = Player("One")
Player_2 = Player("Two")
new_deck = Deck()
new_deck.shuffle()
for x in range(26):
    Player_1.add_cards(new_deck.deal_one())
    Player_2.add_cards(new_deck.deal_one())
round_num = 1
    
while game_on:
    print(f'Round {round_num}')
    round_num += 1     
    if len(Player_1.my_cards) == 0:
        print("Player 1 has no more cards. Game Over!")
        print("Player One Wins!")
        game_on = False
        break
    if len(Player_2.my_cards) == 0:
        print("Player 2 has no more cards. Game Over!")
        print("Player Two Wins!")
        game_on = False
        break
    Player_1_cards =[]
    Player_1_cards.append(Player_1.remove_one())
    Player_2_cards =[]
    Player_2_cards.append(Player_2.remove_one())
    war=True
    
    while war:
        if Player_1_cards[-1].value > Player_2_cards[-1].value:
            Player_1.add_cards(Player_1_cards)
            Player_1.add_cards(Player_2_cards)
            war = False
        
        elif Player_1_cards[-1].value < Player_2_cards[-1].value:
            Player_2.add_cards(Player_1_cards)
            Player_2.add_cards(Player_2_cards)                       
            war = False
        else:
            print('WAR!')
            
            if len(Player_1.my_cards) < 3:
                print("Player One cannot play War! Game over!")
                print("Player Two Wins!")
                game_on = False
                break
            
            elif len(Player_2.my_cards) < 3:
                print("Player Two cannot play War! Game over!")
                print("Player One Wins!")
                game_on = False
                break
            
            else:
                for i in range(3):
                    if len(Player_1.my_cards)>0:
                        Player_1_cards.append(Player_1.remove_one())
                    if len(Player_2.my_cards)>0:
                        Player_2_cards.append(Player_2.remove_one())    