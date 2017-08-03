class Player(object):
    def __init__ (self, name="ME", max_hand_size = 7, mana = 0, health = 20):
        self.name = name
        self.board = []
        self.decks = []
        self.hand = []
        self.grave = []
        self.max_hand_size = max_hand_size
        self.mana = mana
        self.health = health
    def playerDraw(self):
        self.hand.append(self.decks[0].draw())
        return self
    def showHand(self):
        print "{0}'s Hand is:".format(self.name)
        for i in self.hand:
            i.debug()
        return self
    def add(self,deck):
        self.decks.append(deck)
        return self
    def debug(self):
        print "Name:", self.name
        print "Board:", self.board
        print "Deck:", self.decks
        print "Hand:", self.hand
        print "Grave:", self.grave
        print "Max hand size:", self.max_hand_size
        print "Mana:", self.mana
        print "Health:", self.health
        return self
