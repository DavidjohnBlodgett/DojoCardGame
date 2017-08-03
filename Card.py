class Card(object):
    def __init__(self,name,cast,atk = false,defc = false):
        self.name = name
        self.cast = cast
        self.atk = atk
        self.defc = defc
    def debug(self):
        print "#### {0} Debug Output ####".format(self.name)
        print "# Name:",self.name
        print "# Cast:",self.cast
        print "# Attack:",self.atk
        print "# Defence",self.defc
        print "##########################"
        return self

card = Card("White Knight",3,"From the Castle","Kight",2,2)
card.debug()
