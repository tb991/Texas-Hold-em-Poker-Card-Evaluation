import random

print("cards.deck gives you a shuffled deck")

suits = ["D", "C", "H", "S"]

values = ["2","3","4","5","6","7","8","9","T","J","Q","K","A"]

deck = []

for v in values:
	for s in suits:
		deck.append(v + s)

#print(deck)

def shuffle1(deck):
	cardnum1 = random.randint(0,len(deck) - 1) # this is inclusive
	cardnum2 = random.randint(0,len(deck) - 1) # this is inclusive
	cardselected1 = deck[cardnum1]
	cardselected2 = deck[cardnum2]
	deck[cardnum2] = cardselected1
	deck[cardnum1] = cardselected2
	return deck
def go(d):
	d = shuffle1(deck)
	return d

def shuffle120(deck):
	x = 0
	while x < 120:
		deck = go(deck)
		x += 1
	return deck

deck = shuffle120(deck)

def getnew7():
	global deck
	deck = shuffle120(deck)
	return deck[0:7]

# checks if two cards could form a straight
def rank(c):
	rank = -1
	if c[0] == "A":
		rank = 13
	elif c[0] == "K":
		rank = 12
	elif c[0] == "Q":
		rank = 11
	elif c[0] == "J":
		rank = 10
	elif c[0] == "T":
		rank = 9
	else:
		rank = int(c[0]) - 1
	return rank	
def symsToRank(sc):
	out = []
	for c in sc:
		out.append(rank(c[0]))
	out.sort()
	return out
def isStraight1(ranks):
	out = False
	idx = 0
	count = 0
	for x in range(0,5):
		if ranks[x+1] == ranks[x]+1:
			count += 1
	return count >=5
def isStraight(sc):
	x = isStraight1(symsToRank(sc))
	return x
def isFlush(sc):
	count = 0
	out = False
	for x in "DCHS":
		for s in sc:
			if s[1] == x:
				count += 1
		if count >= 5:
			out = True
		count = 0
	return out
def isPairOrMore(sc):
	out = False
	for c in sc:
		for c2 in sc:
			if c == c2:
				pass
			else:
				if c[0] == c2[0]:
					out = True
	return out
