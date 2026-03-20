import cards
import analyze07032026 as evaluator
 
class Player:
	cards = []
	def showCards(self, tableCards):
		return self.cards + tableCards
	def assignCards(self, c1, c2):
		self.cards = [c1, c2]
	def mainScore(self, tableCards):
		if len(self.cards) == 0:
			return ""
		else:
			scoremain = evaluator.go(self.cards + tableCards)
			outcome = ""
			if scoremain == 0:
				outcome = "HIGH CARD"
			elif scoremain == 1:
				outcome = "PAIR"
			elif scoremain == 2:
				outcome = "TWO PAIR"
			elif scoremain == 3:
				outcome = "THREE OF A KIND"
			elif scoremain == 4:
				outcome = "STRAIGHT"
			elif scoremain == 5:
				outcome = "FLUSH"
			elif scoremain == 6:
				outcome = "FULL HOUSE"
			elif scoremain == 7:
				outcome = "FOUR OF A KIND"
			elif scoremain == 8:
				outcome = "STRAIGHT FLUSH"
			print((tableCards + self.cards))
			print(outcome)
# for metabehaviours
class Poker:
	def wideAssign(self, players, deck):
		idx = 0
		for p in players:
			p.assignCards(deck[idx], deck[idx+1])
			idx += 2
	def tableCards(self, deck, numPlayers):
		out = []
		for x in range(0,5):
			out.append(deck[numPlayers*2 + x])
		return out

p1 = Player()
p2 = Player()
p3 = Player()
p4 = Player()
p5 = Player()
p6 = Player()

game = Poker()
deck = cards.deck

game.wideAssign([p1,p2,p3,p4,p5,p6], deck)
tblC = game.tableCards(deck, 6)

p1.mainScore(tblC)
