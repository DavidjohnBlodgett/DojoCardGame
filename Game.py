from Table import Table
from Card import Card
from Deck import Deck
from Player import Player


# gen cards / deck / and 2 players...
table = Table()
deck1 = Deck("BurnDeck","DJ")
deck2 = Deck("CrazyDeck","MATT")
player1 = Player("DJ")
player2 = Player("MATT")

# add cards to decks...
for i in range(0,30):
    deck1.add(Card())
    deck2.add(Card())

# add decks to players...
player1.add(deck1)
player2.add(deck2)

# players draw 7 cards!
player1._firstPlayerDraw()
player2._firstPlayerDraw()


# add players to table...
table.addPlayer(player1).addPlayer(player2)

# play game!
keepPlaying = True
while(keepPlaying):
    keepPlaying = table.nextTurn()

print "Thanks for Playing :)"
