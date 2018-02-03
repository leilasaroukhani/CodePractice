import random


class Card:
    """Represents a standard playing card."""

    def __init__(self, suit=0, rank=2):
        """when we create an object from class Card
         this method gives the values to attributes (suit and rank) """
        self.suit = suit
        self.rank = rank

    # these two are Card class attributes, they are outside of the methodes
    suit_names = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
    rank_names = [None, 'Ace', '2', '3', '4', '5', '6', '7',
                  '8', '9', '10', 'Jack', 'Queen', 'King']

    # when we say print, this method will run
    def __str__(self):
        return '%s of %s' % (Card.rank_names[self.rank],
                             Card.suit_names[self.suit])

    # this method checks between 2 cards, which one has less value. We assume suit are more valuabe than rank
    def __lt__(self, other):
        t1 = self.suit, self.rank
        t2 = other.suit, other.rank
        return t1 < t2

# represens a group of cards
class Deck:

    # we add 52 card object to each deck object with method
    def __init__(self):
        self.cards = []
        for suit in range(4):
            for rank in range(1, 14):
                card = Card(suit, rank)
                self.cards.append(card)

    def __str__(self):
        res = []
        for card in self.cards:
            res.append(str(card))
        return '\n'.join(res)

    # remove one card from  bottem of deck and return it
    def pop_card(self):
        return self.cards.pop()

    # add one card object to the end of deck
    def add_card(self, card):
        self.cards.append(card)

    # change the order of cards in a deck
    def shuffle(self):
        random.shuffle(self.cards)

    def sort(self):
        """Sorts the cards in ascending order."""
        self.cards.sort()

    # I have problem with this function. I could not run it finally
    def remove_card(self, card):
        """Removes a card from the deck or raises exception if it is not there.

        card: Card
        """
        self.cards.remove(card)
    # moving  #num cards from self object (deck) to hand object, which is child of Deck class
    def move_cards(self, hand, num):
        for i in range(num):
            hand.add_card(self.pop_card())

    def deal_hands(self, num_cards=5, num_hands=10):
        """Deals hands from the deck and returns Hands.

        num_cards: cards per hand
        num_hands: number of hands

        returns: list of Hands
        """
        hands = []
        for i in range(num_hands):
            hand = PokerHand()
            self.move_cards(hand, num_cards)
            print(hand, '\n')

            hands.append(hand)
        return hands


class Hand(Deck):
    """Represents a hand of playing cards."""

    def __init__(self, label=''):
        self.cards = []
        self.label = label


# for finding classes that created the method
def find_defining_class(obj, meth_name):
    for ty in type(obj).mro():
        if meth_name in ty.__dict__:
            return ty


class PokerHand(Hand):
    """Represents a poker hand."""

    def suit_hist(self):
        """Builds a histogram of the suits that appear in the hand.

        Stores the result in attribute suits.
        """
        self.suits = {}
        for card in self.cards:
            self.suits[card.suit] = self.suits.get(card.suit, 0) + 1
        return self.suits

    def rank_hist(self):
        """Builds a histogram of the ranks that appear in the hand.

        Stores the result in attribute ranks.
        """
        self.ranks = {}
        for card in self.cards:
            self.ranks[card.rank] = self.ranks.get(card.rank, 0) + 1
        return self.ranks

    def has_pair(self):
        """Returns True if the hand has a pair, False otherwise.

        Note that this works correctly for hands with more than 2 cards.
        """
        self.rank_hist()
        for val in self.ranks.values():
            if val >= 2:
                return True
        return False

    def has_twopair(self):
        """Returns True if the hand has two pair, False otherwise.

        Note that this works correctly for hands with more than 4 cards.
        """
        self.rank_hist()
        for val in self.ranks.values():
            if val >= 2:
                if list(self.ranks.values()).count(val) >= 2:
                    return True
        return False

    def has_threeofakind(self):
        """Returns True if the hand has three of a kind, False otherwise.

        Note that this works correctly for hands with more than 3 cards.
        """
        self.rank_hist()
        for val in self.ranks.values():
            if val >= 3:
                return True
        return False
    #I could not do this
    def has_straight(self):
        """Returns True if the hand has straight, False otherwise.

        Note that this works correctly for hands with more than 5 cards.
        """
        self.rank_hist()
        for key in sorted(self.ranks):
            return True

        return False

    def has_fullhouse(self):

        self.rank_hist()
        for val in self.ranks.values():
            if val >= 3 and list(self.ranks.values()).count(2) >= 1:
                return True
        return False

    def has_fourofakind(self):

        self.rank_hist()
        for val in self.ranks.values():
            if val >= 4:
                return True
        return False

    def has_flush(self):

        self.suit_hist()
        for val in self.suits.values():
            if val >= 4:
                return True
        return False


deck = Deck()
deck.shuffle()
for i in range(7):
    hand = PokerHand()
    deck.move_cards(hand, 7)
    hand.sort()
    print(hand)
    print(hand.rank_hist())
    print(hand.has_pair())
    print('')

for i in range(7):
    hand = PokerHand()
    deck.move_cards(hand, 7)
    hand.sort()
    print(hand)
    print(hand.rank_hist())
    print(hand.has_twopair())
    print('')

for i in range(7):
    hand = PokerHand()
    deck.move_cards(hand, 7)
    hand.sort()
    print(hand)
    print(hand.rank_hist())
    print(hand.has_threeofakind())
    print('')

for i in range(7):
        hand = PokerHand()
        deck.move_cards(hand, 7)
        hand.sort()
        print(hand)
        print(hand.rank_hist())
        print(hand.has_fullhouse())
        print('')

for i in range(7):
        hand = PokerHand()
        deck.move_cards(hand, 7)
        hand.sort()
        print(hand)
        print(hand.rank_hist())
        print(hand.has_fourofakind())
        print('')

for i in range(7):
        hand = PokerHand()
        deck.move_cards(hand, 7)
        hand.sort()
        print(hand)
        print(hand.suit_hist())
        print(hand.has_flush())
        print('')