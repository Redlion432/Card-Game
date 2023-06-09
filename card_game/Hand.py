"""A Hand of playing Card objects"""

class Hand():
    """a hand of playing cards - you can add cards and clear the hand also give cards
    
    Attributes:
        cards (list): a list of card objects"""

    def __init__(self) -> None:
        self.cards = []

    def add(self, card):
        self.cards.append(card)

    def give(self, card, other_hand):
        #remove that card from this hand
        self.cards.remove(card)
        #add that card to the other hand
        other_hand.add(card)

    def clear(self):
        self.cards = []
    
    def __str__(self):
        """print the cards, but only if the hand is not empty"""
        if self.cards:
            representation = ""
            for card in self.cards:
                if not card.is_showing:
                        card.flip()
                representation = card + " "
        else:
            representation = "<empty>"
        return representation
    
if __name__ == "__main__":
    import Card

    # create a hand
    deck = Hand()
    for rank in Card.RANKS:
        for suit in Card.SUITS:
            card = Card.Card(rank, suit)
            deck.add(card)
    print(deck)