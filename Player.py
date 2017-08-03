class Player(object):
    def __init__ (self, name, board, deck, hand, grave, max_hand_size = 7, mana = 1, health = 20):
        self.name = name
        self.board = board
        self.deck = deck
        self.hand = hand
        self.grave = grave
        self.max_hand_size = max_hand_size
        self.mana = mana
        self.health = health

    def debug(self):
        print "'Name' error in Player class:", self.name
        print "'Board' error in Player class:", self.board
        print "'Deck' reference error in Player class:", self.deck
        print "'Hand' error in Player class:", self.hand
        print "'Grave' error in Player class:", self.grave
        print "'Max hand size' error in Player class:", self.max_hand_size
        print "'Mana' error in Player class:", self.mana
        print "'Health' error in Player class:", self.health
        return self
