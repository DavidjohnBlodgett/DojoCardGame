class Player(object):
    def __init__ (self, name, grave, max_hand_size = 7, deck):
        self.name = name
        self.grave = grave
        self.max_hand_size = max_hand_size
        self.deck = deck
    def debug(self):
        print "Name error in Player class:", self.name
        print "Grave error in Player class:", self.grave
        print "Max hand size error in Player class:", self.max_hand_size
        print "Deck reference error in Player class:", self.deck
        return self
