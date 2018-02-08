"""Downey, Think Python, chapter 18, inheritance, exercises."""

import random

class Hist(dict):
    """Map from item to its frequency."""

    def __init__(self, seq=[]):
        for x in seq:
            self.count(x)

    def count(self, x, f=1):
        self[x] = self.get(x, 0) + f
        if self[x] == 0:
            del self[x]


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

    def deal_hands(self, num_hands=10, num_cards=5):
        """Deal hands for a game of poker."""
        hands = []
        for i in range(num_hands):
            hand = Hand()
            self.move_cards(hand, num_cards)
            hand.classify()
            hand.append(hands)


class Hand(Deck):
    """Represent hand of cards, within deck."""

    all_labels = ['straightflush', 'fourkind', 'fullhouse', 'flush',
                  'straight', 'threekind', 'twopair', 'pair', 'highcard']

    def __init__(self, label=''):
        self.cards = []
        self.label = label

    def histogram(self):
        """Make histograms of suits and hands."""
        self.suits = suits
        self.ranks = ranks
        for c in self.cards:
            self.suits.count(c.suit)
            self.ranks.count(c.rank)


    def move_cards(self, hand, num):
        """Move the cards."""
        for i in range(num):
            hand.add_card(self.pop_card())

    def classify(self):
        """Classify the hand; make attributes."""
        self.histogram()
        self.labels = []
        for label in Hand.all_labels:
            f = getattr(self, 'has_' + label)
            if f():
                self.labels.append(label)


def main():
    """."""
    lhist = Hist()
    n = 10000
    for i in range(n):
        if i % 1000 == 0:
            print(i)
        deck = Deck()
        deck.shuffle()
        hands = deck.deal_hands(7, 7)
        for hand in hands:
            for label in hand.labels:
                lhist.count(label)

    total = 7.0 * n
    print(total, 'hands dealt: ')

    for label in Hand.all_labels:
        freq = lhist.get(label, 0)
        if freq == 0:
            continue
        p = total / freq
        print('%s happens one time in %.2f' % (label, p))

if __name__ == '__main__':
    main()
