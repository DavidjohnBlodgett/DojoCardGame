# notes:
# bottom of the deck is index cards[0]
class Deck(object):
    def __init__(self, name, player, max_deck_size = 50):
        # initiates the deck with a deck name, player associated with deck, max deck size, and current deck size. Also creates empty array for holding future cards.
        self.player = player
        self.cards = []
        self.name = name
        self.max_deck_size = max_deck_size
        self.decksize = 0
    def add(self, card):
        # checks if the deck is full then adds card to deck
        if self.max_deck_size < self.decksize+1:
            print "Deck is Full, Cannot add card"
        else:
            self.decksize += 1
            self.cards.append(card)
    def draw(self):
        returnedcard = self.cards[-1]
        self.decksize -= 1
        del self.cards[-1]
        return returnedcard
        pass
    def suffle(self):
        # suffles deck 7 times
        for value in range(0,7):
            random.suffle(self.cards)
    def debug(self):
        # lists all current info for deck
        for value in range(0,len(self.cards)):
            # states all cards in deck as well as their currenty deck index
            print "-------------"
            print self.cards[value].name
            print "index", value
        print "-------------"
        print "Deck Name:", self.name
        print "Player Name:", self.player
        print "max deck size:", self.max_deck_size
        print "decksize:", self.decksize
        print "-------------"
