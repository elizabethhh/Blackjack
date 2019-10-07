#Hello! Welcome to my Blackjack game :)
#Here is how to play: just type run blackjack! It's that easy 

#importing random to get random cards for shuffle
import random

#defining the characteristics of cards
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Ace', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}

#this is going to be a boolean to check if game is still going on
check = True

#Card class
class Card: 
    """A datatype representing a card 
       with an arbitrary suit, rank, and value.
    """

    def __init__(self, suit, rank, value):
        """Constructor for objects of type Card
        """
        self.suit = suit
        self.rank = rank
        self.value = value
    def __str__(self):
        """This method returns a string representation
           for an object of type Card.
        """
        return (self.rank + " of " + self.suit)

#Deck of cards class
class Deck:
    """A datatype representing a deck of 52 cards.
    """

    def __init__(self):
        """Constructor for objects of type deck
        """
        self.deckofCards = []
        for suit in suits:
            for rank in ranks:
                self.deckofCards.append(Card(suit, rank, values[rank]))
    
    def __str__(self):
        """This method returns a string representation
           for an object of type deck.
        """
        #empty string
        deck = ''
        print("These are the cards in deck: ")

        #add card to the empty string
        for i in list(range(len(self.deckofCards))):
            #no comma is last
            if i == len(self.deckofCards) - 1:
                deck += self.deckofCards[i].__str__()
            else:
                deck += self.deckofCards[i].__str__() + ", "
        
        return deck
    
    #shuffle a card
    def shuffle(self):
        """This method shuffles my deck.
        """
        random.shuffle(self.deckofCards)
    
    #get a new card dealed
    def deal(self):
        """This method deals a new card.
        """
        newcard = self.deckofCards.pop()
        return newcard

#Cards in hand class
class Hand:
    """A datatype representing a player's hand of cards.
    """
    def __init__(self):
        """Constructor for objects of type Hand
        """
        self.cards=[]
        self.points = 0
        #edge case of aces in Blackjack!
        self.numberofAces = 0

    def __str__(self):
        """This method returns a string representation
           for an object of type hand.
        """
        alltheCards = ""
        for card in self.cards:
            alltheCards += card + ", "
        return alltheCards

    #adds point value in hand
    def add_card(self,card):
        """This method adds a card.
        """
        self.cards.append(card)
        self.points += values[card.rank]
        if card.rank == "Ace":
            self.numberofAces += 1 #adding number of Aces

    def changeNumofAce(self):
        """This method changes my number of aces if I want to use Ace as point value 1 not 11.
        """
        #check if over 21
        while self.points > 21 and self.numberofAces:
            #reduce from 11 to 1 to consider aces as 1
            self.points -= 10
            self.numberofAces -= 1

    
    

#Chips class
class Chips:
    """A datatype representing a chip class.
    """
    def __init__(self):
        """Constructor for objects of type chips
        """
        self.totalChips = 100
        self.bet = 0
    #if win, more money
    def win(self):
        """Method to add my chip count if I won
        """
        self.totalChips += self.bet
    #if lose, less money
    def lose(self):
        """Method to subtract my chip count if I lose
        """
        self.totalChips -= self.bet



#using try/except 
def take_bet(chips):
    """Method to choose how much you bet
    """
    while True:
        try:
            chips.bet = int(input("You start with 100 chips. How many of these chips are you betting? "))
        except ValueError:
            print("Sorry, only an integer please. ")
        else:
            if chips.bet > chips.totalChips:
                print("Silly you! You don't have that many chips. Try again when you are actually richer. ")
            else:
                #break out of loop
                break
    
#get another card
def hit(deck, hand):
    """Method to get another card
    """
    hand.add_card(deck.deal())
    #checking for ace
    hand.changeNumofAce()

#make choice
def hit_or_stand(deck,hand):
    """Method to choose to stand
    """
    global check
    while True:
        ask = input("Do you want to hit or stand? Type h or s. ")
        if ask.lower() == "h":
            hit(deck, hand)
        elif ask.lower() == "s":
            print("Ok stand by!")
            check = False # no longer playing
        else:
            print("Wrong input! Did your fingers slip? ")
            continue
        break

def show_card(player,dealer):
    """Method to show a card except one of dealers
    """
    print("\nDealer's Hand:")
    print(" <card is hidden>")
    print('',dealer.cards[1])  
    print("\nPlayer's Hand:", *player.cards, sep='\n ')
    
def show_all(player,dealer):
    """Method to show all cards in hand
    """
    print("\nDealer's Hand:", *dealer.cards, sep='\n ')
    print("Dealer's Hand =",dealer.value)
    print("\nPlayer's Hand:", *player.cards, sep='\n ')
    print("Player's Hand =",player.value)

def player_busts(player,dealer,chips):
    """Method when lose
    """
    print("You lost! Guess it wasn't your lucky day - maybe go eat some lucky charms or do something that'll make you luckier")
    chips.lose()

def player_wins(player,dealer,chips):
    """Method when wins
    """
    print("You win! Maybe you're in a better mood now?")
    chips.win()

def dealer_busts(player,dealer,chips):
    """Method if dealer goes over
    """
    print("Ugh I lost! You're lucky today.")
    chips.win()
    
def dealer_wins(player,dealer,chips):
    """Method if dealer wins
    """
    print("Haha I win!! Get on my level :P")
    chips.lose()
    
def push(player,dealer):
    print("Dealer and Player tie! Guess we are both good.")






"""Hosts a game of Blackjack."""
while True: 
    print("Welcome fellow person at Kleiner Perkins! Are you ready to play my game of Blackjack? \nGet close to 21, but don't go over 21! \nI, the dealer, will hit until I get to 17. See if you can beat me! \nFor some background rules, aces are either 1 or 11 depending on what helps you more. \nGood luck :)\n \n")
    deck = Deck()
    deck.shuffle()
    
    playersHand = Hand()
    playersHand.add_card(deck.deal())
    playersHand.add_card(deck.deal())
    
    dealersHand = Hand()
    dealersHand.add_card(deck.deal())
    dealersHand.add_card(deck.deal())

    #get chips
    player_chips = Chips()
    take_bet(player_chips) #bet on it bet on it
    
    show_card(playersHand,dealersHand)

    while check:  #global var

        #asks you do you want to hit and take a risk or settle with what you have
        hit_or_stand(deck,playersHand) 
        
        # one card is hidden from dealer
        show_card(playersHand,dealersHand)  
        
        #game is over
        if playersHand.points > 21:
            player_busts(playersHand,dealersHand,player_chips)
            break        

    #game isn't over...
    if playersHand.points <= 21:
            
        while dealersHand.points < 17:
            hit(deck,dealersHand)    
    
        #show cards
        show_all(playersHand,dealersHand)
        
        #possible situations
        if dealersHand.points > 21:
            dealer_busts(playersHand,dealersHand,player_chips)

        elif dealersHand.points > dealersHand.points:
            dealer_wins(dealersHand,dealersHand,player_chips)

        elif dealersHand.points < dealersHand.points:
            player_wins(dealersHand,dealersHand,player_chips)

        else:
            push(dealersHand,dealersHand)        
        
    #tells them your total
    print("\nPlayer's winnings stand at",player_chips.totalChips)

    keepPlaying = input("You still want to try again? Choose y or n: ")
    
    if keepPlaying.lower()=='y':
        check=True
        continue
    else:

        #tells them that I hope to hear from them
        print('Hope to talk soon! Hope you had fun but if not, maybe play a different game. I recommend fantage.com. ')
        break


