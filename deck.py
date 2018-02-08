"""Downey, Think Python, chapter 18, inheritance, exercises."""

import random

class Card:
    """Represent a stand playing card.

    suits integer codes: Spades: 3, Hearts: 2, Diamonds: 1, Clubs: 0
    face cards integer codes: Jack: 11, Queen: 12, King: 13
    """

    def __init__(self, suit=0, rank=2):
        """Init of class Card."""
        self.suit = suit
        self.rank = rank

    suit_names = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
    rank_names = [None, 'Ace', '2', '3', '4', '5', '6', '7',
                        '8', '9', '10', 'Jack', 'Queen', 'King']

    def __str__(self):
        """Print stuff."""
        return f'{Card.rank_names[self.rank]} of {Card.suit_names[self.suit]}'

    def __lt__(self, other):
        """Check the suits."""
        t1 = self.suit, self.rank
        t2 = other.suit, other.rank
        return t1 < t2


class Deck:
    """Class to define the deck of cards."""

    def __init__(self):
        """Initialize object."""
        self.cards = []
        for suit in range(4):
            for rank in range(1, 14):
                card = Card(suit, rank)
                self.cards.append(card)

    def __str__(self):
        """Print the stuff."""
        res = []
        for card in self.cards:
            res.append(str(card))
        return '\n'.join(res)


    def pop_card(self):
        """Pop card from the bottom, i.e. the last card in list, deck."""
        return self.cards.pop()

    def add_card(self, card):
        """Add card using append method."""
        self.cards.append(card)

    def shuffle(self):
        """Shuffle method from the random module."""
        random.shuffle(self.cards)

    def sort(self):
        """Sort method for deck of cards."""
        self.sort(cards)


