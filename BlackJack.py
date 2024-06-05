import random

suits = ('Hearts','Spades','Diamonds','Clubs')
ranks = ('Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Jack','Queen','King','Ace')
values = {'Two':2,'Three':3,'Four':4,'Five':5,'Six':6,'Seven':7,'Eight':8,'Nine':9,'Ten':10,'Jack':11,'Queen':12,'King':13,'Ace':14}

playing = True

class Card:
    
    def __init__(self,suit,rank):
        self.suit=suit
        self.rank = rank
        self.value = values[self.rank]
    
    def __str__(self):
        return self.rank + ' of ' + self.suit
    
class CardDeck:
    
    def __init__(self):
        self.deck = [] 
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit,rank))
    
    def __str__(self):
        deck_comp = ''
        for card in self.deck:
            deck_comp +='\n' + card.__str__()
        return "The deck contains:" + deck_comp    

    def shuffle(self):
        random.shuffle(self.deck)
        
    def deal(self):
        return self.deck.pop()
    
class Hand:
    
    def __init__(self):
        self.cards = []  
        self.value = 0   
        self.aces = 0    
    
    def add_card(self,card):
        self.cards.append(card)
        self.value += values[card.rank]
        if card.rank == 'Ace':
            self.aced += 1
    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -=1
            
class Chips:
    
    def __init__(self,total=100):
        self.total = total
        self.bet = 0
        
    def win_bet(self):
        self.total += self.bet
    
    def lose_bet(self):
        self.total -= self.bet
        
def take_bet(chips):
    while True:
        try:
            chips.bet = int(input("Place your bet: "))
        except ValueError:
            print("Please enter an integer")
        else:
            if chips.bet > chips.total:
                print(f"Sorry, your bet exceeds your total chips! Place under {chips.total}")        
            else:
                break
            
def hit(deck,hand):
    hand.add_card(deck.deal())        
    hand.adjust_for_ace()
    
def hit_or_stand(deck,hand):
    global playing
    while True:
        x=input('Hit or Stand? Enter H or S: ')
        if x[0].lower() == 'h':
            hit(deck,hand)
        elif x[0].lower() == 's':
            print("Dealer's Turn")
            playing = False
        else:
            print("Please enter H or S only!")
            continue   
        break     

def show_some(player,dealer):
    print("\nDealer's Hand: ")
    print("First card hidden!")
    print(dealer.cards[1])
    
    print("\nPlayer's Hand: ")
    for card in player.cards:
        print(card)
    print("Current score is: {}".format(player.value))    
    
def show_all(player,dealer):
    print("\n Dealer's Hand: ")
    for card in dealer.cards:
        print(card) 
    print(f"Value of Dealer's hand is: {dealer.value}")
        
    print("\n Player's Hand: ")
    for card in player.cards:
        print(card)
    print(f"Value of Player's hand is: {player.value}")
    
def player_busts(chips):
    print("Player Bust!")
    chips.lose_bet()

def player_wins(chips):
    print('Player Wins!')
    chips.win_bet()

def dealer_busts(chips):
    print('Dealer Busts! Player Wins!')
    chips.win_bet()
    
def dealer_wins(chips):
    print('Dealer Wins!')
    chips.lose_bet()
    
def push():
    print("It's a tie! PUSH")           
   
while True:
    print("Welcome to BlackJack!")
    deck=CardDeck()
    deck.shuffle()
    
    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())
    
    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())

    player_chips = Chips(250)
    
    take_bet(player_chips)
    
    show_some(player_hand,dealer_hand)
    
    while playing:
        hit_or_stand(deck,player_hand)
        show_some(player_hand,dealer_hand)
        if player_hand.value > 21:
            player_busts(player_chips)
            break

    if player_hand.value <= 21:
        while dealer_hand.value < 17:
            hit(deck,dealer_hand)
        show_all(player_hand,dealer_hand)
        if dealer_hand.value > 21:
            dealer_busts(player_chips)
        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_chips)
        elif dealer_hand.value < player_hand.value:
            player_wins(player_chips)
        else:
            push()            
        
    print('\n Player current chips are at:{}'.format(player_chips.total))
    
    new_game = input("Would you like to play again? Y or N : ")
    if new_game[0].lower() == 'y':
        playing = True
    else:
        print('Thank you for playing.')
        break    