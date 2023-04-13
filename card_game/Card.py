"""
Name: Card.py
Author: Jake Russell
Purpose: Represents a card in a card game.
"""

class Card:
    """A card in a card game (can server as a base class for other types of
    card games).
    
    This is a typical card from a Bicycle/Hoyle type card deck like you would
    use in a BlackJack, Poker type card game.
    
    Attributes:
        RANKS: (tuple): possible card ranks (str)
        rank: (str): represents the current card's rank
        SUITS: (tuple): of card Suits (str)
        suits: (str): the current card's suit
        is_showing: (bool): can we see the rank and suit of a card
        """
    RANKS = ("Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", 
             "Queen", "King")
    SUITS = ("Clubs", "Hearts", "Spades", "Diamonds")

    # Constructor
    def __init__(self, rank: str, suit: str) -> None:
        self.rank = rank
        self.suit = suit
        self.is_showing = False

    def flip(self):
        self.is_showing = not self.is_showing


    def __str__(self):
        representation = ""
        if self.is_showing:
            representation = self.rank + " of " + self.suit
        else:
            representation = "back of card"
        return representation

if __name__ == "__main__":
    card1 = Card("Ace", "Spades")
    print(card1.rank)
    print(card1.suit)
    card1.flip()
    print(card1)
    card1.flip()
    print(card1)