import basics as b
# "basics" includes addPlayers(n), addPlayer(), removePlayer(n), deal(), shuffle(), deck, players, tableCards
# players is a list of elements, each element will have two cards after deal() is run
# tableCards is a list of five cards

# returns True if there's at least two cards of the same order
def pair(table, hand):
	return toak(table, hand, 2)==1
# toak() is used used for pair, two pair, TOAK and FOAK
# for two pair output should be 2, others 1
# matchNumber: 2 for pair/twopair, 3 for 3oak, 4 for 4oak
# it is also used in the full house function
def toak(table, hand, matchNumber):
	cs = table + hand
	# need to rule out pairs counting twice
	# lists unique cards
	# then counts them
	# then returns if there are three of any
	matches = []
	idx = 0
	for c1 in cs:
		if c1[0] in matches:
			pass
		else:
			matches.append(c1[0])
			idx += 1
	counts = [0]*len(matches)
	x = 0
	while x < len(matches):
		y = 0
		while y < len(cs):
			 if cs[y][0] == matches[x]:
			 	counts[x] += 1
			 y+=1
		x+=1
	# extend so it can distinguish pairs and two pairs
	countOfMatches = 0
	c = 0
	while c < len(counts):
		if counts[c]==matchNumber:
			countOfMatches+=1
		c+=1
	return countOfMatches
# checks if there's a straight for the player
def straight(table, hand):
	cs = table + hand
	x = 0
	order = "A" + b.order
	givenOrders = ""
	i = 0
	# get the order/value of every card and put it in a string
	while i < len(cs):
		givenOrders += cs[i][0]
		i += 1
	# loop over A23456...
	straightFound = False
	while x < len(order)-4:
		y = 0
		run = True
		while y < 5:
			#print(order[x + y], end="")
			if order[x + y] not in givenOrders:
				run = False
			y += 1
		#print("")
		if run:
			straightFound = True
		x += 1
	return straightFound
def flush(table, hand):
	cs = table + hand
	suits = b.suits
	givenSuits = ""
	i = 0
	# get all suits given
	while i < len(cs):
		givenSuits += cs[i][1]
		i += 1
	flushFound = False
	for s in suits:
		if givenSuits.count(s)>=5:
			flushFound = True
	return flushFound
def strFlush(table, hand):
	#(this is the flush function subsequently merged with a modified straight function)
	# first identify the flush
	# gather all these cards
	cs = table + hand
	suits = b.suits
	givenSuits = ""
	i = 0
	while i < len(cs):
		givenSuits += cs[i][1]
		i += 1
	flushFound = False
	suit = ""
	sf = False
	for s in suits:
		if givenSuits.count(s)>=5:
			flushFound = True
			suit = s # thankfully we can't get two flushes in one hand
	# then detect a straight in them
	if flushFound:
		suited = []
		for c in cs:
			if c[1]==suit:
				suited.append(c)
		sf = straight([suited[0]], suited[1:])
	return sf
def fh(table, hand):
	two = toak(table, hand, 2) 
	three = toak(table, hand, 3)
	return three==2 or (three==1 and two==1)
def determine(table, hand):
	p = pair(table, hand)==1
	twopair = toak(table, hand, 2)==2
	threeoak = toak(table, hand, 3)>=1
	strayt = straight(table, hand)
	fl = flush(table, hand)
	fullhouse = fh(table, hand)
	fouroak = toak(table, hand, 4)==1
	strflush = strFlush(table, hand)
	a = [p, twopair, threeoak, strayt, fl, fullhouse, fouroak, strflush]
	#print(a)
	if strflush:
		print("STRAIGHT FLUSH")
	elif fouroak:
		print("FOUR OF A KIND")
	elif fullhouse:
		print("FULL HOUSE")
	elif fl:
		print("FLUSH")
	elif strayt:
		print("STRAIGHT")
	elif threeoak:
		print("THREE OF A KIND")
	elif twopair:
		print("TWO PAIR")
	elif p:
		print("PAIR")
	else:
		print("HIGH CARD")
