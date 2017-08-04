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
        drawnCard = self.decks[0].draw()
        self.hand.append(drawnCard)
        print "You drew ", drawnCard.debug()
        return self
    def _firstPlayerDraw(self):
        for i in range(0,7):
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
    def playCard(self, card_name):
        # removes a specific card in the deck by name
        for card in range(0, len(self.hand)):
            if self.hand[card].name == card_name:
                self.board.append(self.hand[card])
                del self.hand[card]
    def isInHand(self,card_name):
        result = False
        for card in self.hand:
            if card.name is card_name:
                result = True
        return result
    # private functions...
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
