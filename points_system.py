'''
It may not be as complicated as I'm making it, but determining if a certain flush is bigger than another flush, or a pair bigger than another pair etcs is a cause of annoyance for me. I'm going to create a points system to simplify it in my mind.

FOR HIGH CARD
Rather than using numbers I can use a bit field with values from 0 to 4.
There are 13 values for high card, so I need 13 zeroes to start with.
[two, three, four, five, six, seven, eight, nine, ten, jack, queen, king, ace]
or value = [0]*13
don't need to select the five highest cards, just calculate for the seven
'''
# high cards can be compared by value
# flushes can be compared by value
# straights can be compared by value
# pairs
# all hands can be evaluated so long as they are different by rank (pair, two pair etc)
import basics as b
def highCardValuator(table, hand):
	cs = table + hand
	i = 0
	value = [0]*len(b.order)
	while i < len(cs):
		v = cs[i][0]
		incV(value, v)
		i += 1
	return value
# adjusts the bit field for the card to produce its relative value	
def incV(vals, cardVal):
	j = 0
	while j < len(b.order):
		if b.order[j]==cardVal:
			vals[j] += 1
		j += 1
	return vals
# compares to high card valuations and says which argument wins
def determineWinner(vals1, vals2):
	x = len(vals1)-1
	n = 0
	winner = -1
	while x >= 0:
		n = vals1[x]-vals2[x]
		if n > 0:
			winner = 1
		elif n < 0:
			winner = 0
		x -= 1
	return winner
	# -1: draw, 0: player associated with vals1 wins, 1: vals2 wins 
def testHCV():
	table = ["AS", "KS", "QS", "TD",  "9D"]
	hand = ["8D", "6C"]
	out = [0, 0, 0, 0,1, 0, 1, 1, 1, 0, 1, 1, 1]
	assert highCardValuator(table, hand)==out, "High card evaluation fails 1"
	table = ["2S", "2H", "4C", "4D",  "6S"]
	hand = ["6H", "8D"]
	out = [2,0,2,0,2,0,1,0,0,0,0,0,0]
	assert highCardValuator(table, hand)==out, "High card evaluation fails 2"
	table = ["AS", "AH", "AC", "AD",  "KS"]
	hand = ["KH", "KC"]
	out = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 4]
	assert highCardValuator(table, hand)==out, "High card evaluation fails 3"
	table = ["AS", "KS", "QS", "TD",  "2D"]
	hand1 = ["8D", "6C"]
	hand2 = ["9D", "6S"]
	a = highCardValuator(table, hand1)
	b = highCardValuator(table, hand2)
	assert determineWinner(a,b)==1, "Determining the winner fails 1"
	assert determineWinner(b,a)==0, "Determining the winner fails 2"
testHCV()
def hcv5card(cards):
	return highCardValuator([cards[0]], cards[1:])
def testH5():
	cards = ["AS", "KS", "QS", "TS",  "9S"]
	out = [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1]
	assert hcv5card(cards)==out, "Flush value evaluation fails 1"
	cards = ["AS", "2S", "5S", "4S",  "3D"]
	out = [1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1]
	assert hcv5card(cards)==out, "Straight value evaluation fails 1"
testH5()
# hands is a list of 2-element lists representing the cards each player has, table is the table cards
import HandEval as h
ranks = ["HIGH CARD", "PAIR", "TWO PAIR", "THREE OF A KIND", "STRAIGHT", "FLUSH", "FULL HOUSE", "FOUR OF A KIND", "STRAIGHT FLUSH"]
def evaluate(table, hands):
	valuation = []
	numVal = [0]*len(hands)
	for ha in hands:
		valuation.append(h.determine(table, ha))
	i = 0
	highestRank = -1
	winners = [0]*len(hands)
	for v in valuation:
		i = 0
		while i < len(ranks):
			if v == ranks[i] and i > highestRank:
				highestRank = i
			i += 1
	#print(highestRank)
	idx = 0
	for v in valuation:
		#print(v)
		if v==ranks[highestRank]:
			winners[idx] = 1
		idx +=1
	# all winners up to here are not necessarily the winners, only so if their hands are equivalent
	# here belongs the comparison of similar hands
	if ranks[highestRank]=="HIGH CARD":
		vals = []
		for ha in hands:
			vals.append(highCardValuator(table, ha))
		# vals now contains [0,1,1,0.. etc] representing how many of each card appear in the hand
		# if each index has a number associated with it that cannot be trumped by prior numbers when multiplied by the amount ...
		# then the accumulation of the numbers represents its relative value
		# for high card these numbers work
		relVal = [[]]*len(vals)
		i = 0
		# give each card a kind of monetary value
		while i < len(relVal):
			j = 0
			while j < len(vals[i]):
				relVal[i] = relVal[i] + [(1*10**j)*vals[i][j]]
				j += 1
			i += 1
		i = 0
		winnerVal = 0
		points = [0]*len(relVal)
		# sum up each monetary value (to one value per player)
		while i < len(points):
			points[i] = sum(relVal[i])
			if points[i] > winnerVal:
				winnerVal = points[i]
			i+=1
		i = 0
		# set who has won based on their "money"
		while i < len(points):
			if points[i] == winnerVal:
				points[i] = 1
			else:
				points[i] = 0
			i+=1
		winners = points
	elif ranks[highestRank]=="PAIR":
		print("boo2")
	elif ranks[highestRank]=="TWO PAIR":
		print("boo3")
	elif ranks[highestRank]=="THREE OF A KIND":
		print("boo4")
	elif ranks[highestRank]=="STRAIGHT":
		print("boo5")
	elif ranks[highestRank]=="FLUSH":
		print("boo6")
	elif ranks[highestRank]=="FULL HOUSE":
		print("boo7")
	elif ranks[highestRank]=="FOUR OF A KIND":
		print("boo8")
	elif ranks[highestRank]=="STRAIGHT FLUSH":
		print("boo9")
	return winners	
	
def genTest():
	table = ["AS", "KS", "QS", "TS",  "9H"]
	hands = [["2H", "3H"], ["JC", "2C"]]
	assert evaluate(table, hands)==[0,1], "A hand ranking has failed 1"
	hands = [["2H", "3H"], ["JC", "2C"], ["2S", "7D"]]
	assert evaluate(table, hands)==[0,0,1], "A hand ranking has failed 2"
	hands = [["2H", "3H"], ["JC", "2C"], ["JD", "2H"]]
	assert evaluate(table, hands)==[0,1,1], "A hand ranking has failed 3"
	table = ["AS", "KS", "4D", "TS",  "9H"]
	hands = [["2H", "3H"], ["8D", "2C"]]
	assert evaluate(table, hands)==[0,1], "High cards valuation fails 1"
	table = ["8H", "2S", "3D", "4S",  "5H"]
	hands = [["TH", "9S"], ["7S", "9H"]]
	assert evaluate(table, hands)==[1,0], "High cards valuation fails 2"
	table = ["AS", "KS", "4D", "TS",  "9H"]
	hands = [["AH", "3H"], ["KD", "2C"]]
	assert evaluate(table, hands)==[0,1], "Pairs valuation fails"
	table = ["AS", "KS", "4D", "TS",  "9H"]
	hands = [["9S", "KC"], ["KD", "4C"]]
	assert evaluate(table, hands)==[0,1], "Two pairs valuation fails"
	table = ["AS", "KS", "4D", "TS",  "9H"]
	hands = [["KS", "KC"], ["AD", "AC"], ["9D", "8H"]]
	assert evaluate(table, hands)==[0, 1, 0], "Three of a kind valuation fails"
	table = ["2S", "KS", "QD", "TS",  "9H"]
	hands = [["JS", "KC"], ["AD", "JC"], ["9D", "8H"]]
	assert evaluate(table, hands)==[0, 1, 0], "Straight valuation fails"
	table = ["AS", "KS", "4S", "TD",  "9H"]
	hands = [["3S", "9S"], ["AD", "AC"], ["4S", "8S"]]
	assert evaluate(table, hands)==[1, 0, 0], "Flush valuation fails"
	table = ["AS", "KS", "AD", "TS",  "9H"]
	hands = [["9D", "AC"], ["AH", "KD"], ["TD", "TH"]]
	assert evaluate(table, hands)==[0, 1, 0], "Full house valuation fails"
	table = ["AS", "AH", "JC", "JH",  "9H"]
	hands = [["AD", "AC"], ["JD", "JS"], ["TD", "TH"]]
	assert evaluate(table, hands)==[1, 0, 0], "Four of a kind valuation fails"
	table = ["5S", "3S", "4S", "AH",  "KH"]
	hands = [["2S", "AS"], ["6S", "7S"], ["TD", "TH"]]
	assert evaluate(table, hands)==[0, 1, 0], "Straight-flush valuation fails"
genTest()
