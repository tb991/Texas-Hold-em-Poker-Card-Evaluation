'''
this file handles the basics of Texas Hold'Em Poker, such as adding/removing players and dealing
'''
print("Hello world.")
tableCards = []
suits = "DCHS"
order = "23456789TJQKA"
# cardString should be the card to add, cards is a mutable argument and should be tableCards
def addTableCard(cardString, cards):
	repeat = cardString in tableCards
	validSuit = cardString[1] in suits
	validOrder = cardString[0] in order
	tableFull = len(tableCards) >= 5
	worked = False
	if not repeat and validSuit and validOrder and not tableFull:
		cards.append(cardString)
		worked = True
	else:
		worked = False
	return worked

players = []
# removes a player by his number, by the order he was added to the table, starting with 1
def removePlayer(playerNumber):
	out = False
	if playerNumber <= len(players):
		players.pop(playerNumber-1)
		out = True
	else:
		out = False
	return out
playerLimit = 9	
# adds a player to the table with an empty hand
def addPlayer():
	out = False
	if len(players) < playerLimit:
		players.append([])
		out = True
	return out
# generate and shuffle deck
deck = []
for o in order:
	for s in suits:
		deck.append(o + s)
import random
# uses a Fisher-Yates shuffle to efficiently shuffle the deck
def shuffle():
	global deck
	x = len(deck) - 1
	y = 0
	while x > 0:
		y = random.randint(0,x-1)
		b = deck[y]
		deck[y] = deck[x]
		deck[x] = b
		x-=1
shuffle()
# deals cards to any players, as long as there are 2 or more present
def deal():
	out = False
	if len(players) < 2:
		out = False
	for p in players:
		if p != []:
			out = False
	limit = len(players)*2
	x = 0
	while x < limit:
		playerIdx = x%len(players)
		cardIdx = x%2
		players[playerIdx].append(deck[x])
		x += 1
	print("Player hands after dealing: ")
	print(players)
# deletes all players and then adds however many specified
def addPlayers(number):
	global players
	players = []
	for x in range(0,number):
		addPlayer()
