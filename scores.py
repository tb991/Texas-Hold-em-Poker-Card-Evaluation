# ranking a hand based on strength of relevant cards

def rankStrength(sc, numCards, isFlush, relevantSuit):
	ranks = "AKQJT98765432"
	fiveCards = []
	idx = 0
	suit = ""
	if isFlush:
		suit = relevantSuit
	for r in ranks:
		for c in sc:
			if (isFlush and c[1] == suit and r == c[0]) or (not isFlush and r == c[0]):
				fiveCards.append(r)
		if len(fiveCards) == numCards:
			break
	score = 0
	vals = ["2","3","4","5","6","7","8","9","T","J","Q","K","A"]
	for f in fiveCards: # making this OUT rather than foundOrdered means it doesn't count redundant cards in the score
		score += vals.index(f[0]) + 1
	return score
def highcard(sc):
	return rankStrength(sc, 5, False, "")
def pair(sc):
	# get the repeated rank (there can only be one)
	ranks = []
	for c in sc:
		ranks.append(c[0])
	repeatedRank = ""
	otherRanks = ""
	for r in ranks:
		if ranks.count(r) == 2:
			repeatedRank = r
		else:
			# get all other ranks
			otherRanks += r
	# delete the last two ranks
	count = 0
	otherRanksMinus = ""
	i = 0
	for r in "AKQJT98765432":
		if otherRanks[i] == r:
			otherRanksMinus += r
			i += 1
		if len(otherRanksMinus) == len(otherRanks) - 2:
			break 
	# compute the score
	vals = ["2","3","4","5","6","7","8","9","T","J","Q","K","A"]
	score = 0
	bigFactor = 100
	score += (vals.index(repeatedRank)+1) * bigFactor
	for r in otherRanksMinus:
		score += vals.index(r) + 1
	return score
# sort string by rank, also removes duplicates
def ssbr(string):
	r = "AKQJT98765432"
	out = ""
	for x in r:
		if x in string:
			out += x
	return out
def twopair(sc):
	# get the repeated rank (there can only be one)
	ranks = []
	for c in sc:
		ranks.append(c[0])
	repeatedRanks = ""
	otherRanks = ""
	for r in ranks:
		if ranks.count(r) == 2 and r not in repeatedRanks:
			repeatedRanks += r
		elif ranks.count(r) == 1:
			# get all other ranks
			if r not in otherRanks:
				otherRanks += r
	# if the length of the repeated ranks is 3 (3 pairs) then remove the lowest and
	# put it in otherRanks
	if len(repeatedRanks) == 3:
		extra = ssbr(repeatedRanks)[-1]
		print(extra + " :) ")
		otherRanks += extra
		repeatedRanks = ssbr(repeatedRanks)[0:-1]
	# delete all but the top rank from otherRanks
	count = 0
	otherRanksMinus = ""
	i = 0
	for r in "AKQJT98765432":
		if r in otherRanks:
			otherRanksMinus = r
			break
	# compute the score
	vals = ["2","3","4","5","6","7","8","9","T","J","Q","K","A"]
	score = 0
	bigFactor = 100
	print(repeatedRanks)
	score += (vals.index(repeatedRanks[0])+1) * bigFactor
	score += (vals.index(repeatedRanks[1])+1) * bigFactor
	for r in otherRanksMinus:
		score += vals.index(r) + 1
	return score
def toak(sc):
	# get the repeated rank (there can only be one)
	ranks = []
	for c in sc:
		ranks.append(c[0])
	repeatedRank = ""
	otherRanks = ""
	for r in ranks:
		if ranks.count(r) == 3:
			repeatedRank = r
		else:
			# get all other ranks
			otherRanks += r
	# sort the otherRanks and only keep 2 top
	otherRanks = ssbr(otherRanks)[0:2]
	# compute the score
	vals = ["2","3","4","5","6","7","8","9","T","J","Q","K","A"]
	score = 0
	bigFactor = 100
	score += (vals.index(repeatedRank)+1) * bigFactor
	for r in otherRanks:
		score += vals.index(r) + 1
	return score
def foak(sc):
	# get the repeated rank (there can only be one)
	ranks = []
	for c in sc:
		ranks.append(c[0])
	repeatedRank = ""
	otherRanks = ""
	for r in ranks:
		if ranks.count(r) == 4:
			repeatedRank = r
		else:
			# get all other ranks
			otherRanks += r
	# sort the otherRanks and only keep 2 top
	otherRanks = ssbr(otherRanks)[0]
	# compute the score
	vals = ["2","3","4","5","6","7","8","9","T","J","Q","K","A"]
	score = 0
	bigFactor = 100
	score += (vals.index(repeatedRank)+1) * bigFactor
	for r in otherRanks:
		score += vals.index(r) + 1
	return score
def fullhouse(sc):
	# get the repeated rank (there can only be one)
	ranks = []
	for c in sc:
		ranks.append(c[0])
	repeatedRank = ""
	otherRanks = ""
	for r in ranks:
		if ranks.count(r) == 3:
			repeatedRank = r
		elif ranks.count(r) == 2:
			# get all other ranks
			otherRanks += r
	# sort the otherRanks and only keep 2 top
	otherRanks = ssbr(otherRanks)[0]
	# compute the score
	vals = ["2","3","4","5","6","7","8","9","T","J","Q","K","A"]
	score = 0
	bigFactor = 100
	score += (vals.index(repeatedRank)+1) * bigFactor
	for r in otherRanks:
		score += vals.index(r) + 1
	return score
def flush(sc):
	idx = 0
	suits = [0,0,0,0]
	suit = ""
	for s in "SHCD":
		for c in sc:
			if c[1] == s:
				suits[idx] += 1
		idx += 1
	for count in suits:
		if count >= 5:
			suit = "SHCD"[suits.index(count)]
	return rankStrength(sc, 5, True, suit)
def straight(sc):
	ranks = ""
	for c in sc:
		ranks += c[0]
	ranks = ssbr(ranks)
	length = len(ranks)
	score = 0
	diff = length - 5
	count = 0
	matches = []
	possibilities = ["AKQJT", "KQJT9", "QJT98", "JT987", "T9876", "98765", "87654"]
	possibilities = possibilities + ["76543", "65432", "A5432"]
	while count <= diff:
		match = ranks[count:(count + 5)]
		if match in possibilities:
			score = 11 - ((possibilities.index(match) + 1))
		count += 1
	return score
def strFlush(sc):
	# find suit
	idx = 0
	suits = [0,0,0,0]
	suit = ""
	for s in "SHCD":
		for c in sc:
			if c[1] == s:
				suits[idx] += 1
		idx += 1
	for count in suits:
		if count >= 5:
			suit = "SHCD"[suits.index(count)]
	# suit founded
	ranks = ""
	for c in sc:
		if c[1] == suit:
			ranks += c[0]
	ranks = ssbr(ranks)
	length = len(ranks)
	score = 0
	diff = length - 5
	count = 0
	matches = []
	possibilities = ["AKQJT", "KQJT9", "QJT98", "JT987", "T9876", "98765", "87654"]
	possibilities = possibilities + ["76543", "65432", "A5432"]
	while count <= diff:
		match = ranks[count:(count + 5)]
		if match in possibilities:
			score = 11 - ((possibilities.index(match) + 1))
			break # this break is important to ignore extra cards
		count += 1
	return score	
