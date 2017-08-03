class Table(object):
    def __init__(self):
        self.players = []
        self.turnCount = 0
        self.turnPhase = 0
        self.playerIndex = 0
    def addPlayer(self,player):
        self.players.append(player)
        return self
    def outputScreen(self):
        print "I printed the board!"
        return self

    # GAME LOGIC FUNCTIONS
    def getMana(self,player):
        player.mana += 1
        print "{0} Mana now is: {1}".format(player.name,player.mana)
        pass
    def untapCards(self,player):
        # player.board.cards status = untap
        print "untapCards"
        pass
    def drawCard(self,player):
        player.playerDraw()
        player.showHand()
        pass
    def playCard(self,player):
        print "playCard"
        pass
    def combat(self,player):
        print "combat"
        pass
    def endTurn(self):
        print "endTurn"
        return 1
    def nextTurn(self):
        print "I started the game"
        # userInput = raw_input("Please enter something: ")
        # print userInput
        self.getMana(self.players[self.playerIndex])
        self.untapCards(self.players[self.playerIndex])
        self.drawCard(self.players[self.playerIndex])
        self.playCard(self.players[self.playerIndex])
        self.combat(self.players[self.playerIndex])
        self.playerIndex = self.endTurn()
        print "The next player is:", self.playerIndex
        return False


    # OTHER LOGIC FUNCTIONS
    def checkDeath(self,player):
        pass
    def winState(self,player):
        pass
    def debug(self):
        print "##### PLAYER DEBUG #####"
        print "Players:",self.players
        print "Turn Count:",self.turnCount
        print "Turn Phase:",self.turnPhase
        return self
