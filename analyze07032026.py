# purpose of this file is to look at 7 available cards and call relevant functions to check what the player has


sevencards1 = ["2S","2D","3H","3C","4S","4H", "4D"] # sample for testing
sevencards2 = ["2S","3D","5H","6C","AS","QH", "TH"] # sample for testing
sevencards3 = ["2S","2D","5H","2C","AS","2H", "TH"] # sample for testing
sevencards4 = ["AS","AD","AH","2C","7S","2H", "7H"] # sample for testing
sevencards20 = ["2S","2D","3H","3C","4S","6H", "8D"] # sample for testing
sevencards21 = ["2S","2D","5H","AC","AS","5D", "TH"] # sample for testing
sevencards22 = ["2S","9D","7H","2C","7S","2H", "7H"] # sample for testing

def score(sc):
	ranks = "AKQJT98765432"
	fiveCards = []
	idx = 0
	for r in ranks:
		for c in sc:
			if r == c[0]:
				fiveCards.append(r)
		if len(fiveCards) == 5:
			break
	score = 0
	vals = ["2","3","4","5","6","7","8","9","T","J","Q","K","A"]
	for f in fiveCards: # making this OUT rather than foundOrdered means it doesn't count redundant cards in the score
		score += vals.index(f[0]) + 1
	return score
#print(score(sevencards1))
def boolPrint(sc):
	x1 = pair(sc) # [0] == 1
	x2 = toak(sc) # True
	x3 = twopair(sc) # [0] == True
	x4 = fullhouse(sc) # [0] == True
	x5 = foak(sc) # True
	x6 = straight(sc) # len() == 5
	x7 = flush(sc) # [0] == True
	x8 = strFlush(sc) # True
	print([x1,x2,x3,x4,x5,x6,x7,x8])
def highcard(sc):
	x1 = pair(sc) # [0] == 1
	x2 = toak(sc) # True
	x3 = twopair(sc) # [0] == True
	x4 = fullhouse(sc) # [0] == True
	x5 = foak(sc) # True
	x6 = straight(sc) # len() == 5
	x7 = flush(sc) # [0] == True
	x8 = strFlush(sc) # True
	out = ""
	#print(bigOut)
	if x1[0]!=0 or x2 or x3[0] or x4[0] or x5 or len(x6) != 5 or x7[0] or x8:
		out = False 
	else:
		out = True
	return out
def pair(sc):
	x = 0
	bin = []
	while x < len(sc):
		if sc[x][0] not in bin:
			bin.append(sc[x][0])
		x += 1
	counts = [0]*len(bin)
	x = 0
	while x < len(sc):
		if sc[x][0] in bin:
			counts[bin.index(sc[x][0])] += 1
		x += 1
	# now need to count the score of the pair and high cards
	ranks = "AKQJT98765432"
	fiveCards = []
	if 2 in counts:
		fiveCards.append(bin[counts.index(2)])
		fiveCards.append(bin[counts.index(2)])
	idx = 0
	for r in ranks:
		for c in sc:
			if r == c[0] and c[0] not in fiveCards:
				fiveCards.append(r)
		if len(fiveCards) == 5:
			break
	score = 0
	vals = ["2","3","4","5","6","7","8","9","T","J","Q","K","A"]
	bigFactor = 100
	for f in fiveCards: # making this OUT rather than foundOrdered means it doesn't count redundant cards in the score
		if 2 in counts:
			if f == bin[counts.index(2)]:
				score += (vals.index(f[0]) + 1)*100
				pass
			else:
				score += vals.index(f[0]) + 1
	return [counts.count(2), score]
'''
print(pair(sevencards1))
print(pair(sevencards2))
print(pair(sevencards3))
print(pair(sevencards4))
'''
def twopair(sc):
	x = 0
	bin = []
	while x < len(sc):
		if sc[x][0] not in bin:
			bin.append(sc[x][0])
		x += 1
	counts = [0]*len(bin)
	x = 0
	while x < len(sc):
		if sc[x][0] in bin:
			counts[bin.index(sc[x][0])] += 1
		x += 1
	# now need to count the score of the pair and high cards
	ranks = "AKQJT98765432"
	fiveCards = []
	if 2 in counts:
		fiveCards.append(bin[counts.index(2)])
		fiveCards.append(bin[counts.index(2)])
	idx = 0
	for r in ranks:
		for c in sc:
			if r == c[0] and c[0] not in fiveCards:
				fiveCards.append(r)
		if len(fiveCards) == 5:
			break
	score = 0
	vals = ["2","3","4","5","6","7","8","9","T","J","Q","K","A"]
	bigFactor = 100
	for f in fiveCards: # making this OUT rather than foundOrdered means it doesn't count redundant cards in the score
		if 2 in counts:
			if f == bin[counts.index(2)]:
				score += (vals.index(f[0]) + 1)*100
				pass
			else:
				score += vals.index(f[0]) + 1
	return counts.count(2)==2 or counts.count(2)==3
'''
print(twopair(sevencards1))
print(twopair(sevencards2))
print(twopair(sevencards3))
print(twopair(sevencards4))
print(twopair(sevencards20))
print(twopair(sevencards21))
print(twopair(sevencards22))
'''
def toak(sc):
	x = 0
	bin = []
	while x < len(sc):
		if sc[x][0] not in bin:
			bin.append(sc[x][0])
		x += 1
	counts = [0]*len(bin)
	x = 0
	while x < len(sc):
		if sc[x][0] in bin:
			counts[bin.index(sc[x][0])] += 1
		x += 1
	#print(counts)
	return counts.count(3)==1 or counts.count(3)==2
def count(sc):
	ranks = "23456789TJQKA"
	rankCounts = [0]*len(ranks)
	for x in sc:
		indexOfRank = ranks.index(x[0])
		rankCounts[indexOfRank] += 1
	return rankCounts
def fullhouse(sc):
	counts = count(sc)
	ranks = "23456789TJQKA"
	pairRank = ""
	toakRank = ""
	x = 0
	out = ""
	while x < len(ranks):
		if counts[x] == 2:
			pairRank = ranks[x]
		if counts[x] == 3:
			toakRank = ranks[x]
		x += 1
	fiveCards = []
	for c in sc:
		if c[0] != pairRank and c[0] != toakRank:
			pass
		else:
			fiveCards.append(c)
	score = 0
	vals = ["2","3","4","5","6","7","8","9","T","J","Q","K","A"]
	bigFactor = 0 # i need to make the three of a kind much more valuable than the pair
	for f in fiveCards: # making this OUT rather than foundOrdered means it doesn't count redundant cards in the score
		if f[0] == toakRank:
			bigFactor = 100
		score += (vals.index(f[0]) + 1) * bigFactor
	if pairRank != "" and toakRank != "":
		out = [True, pairRank, toakRank, score]
	else:
		out = [False, "", "", 0]
	return out
'''
print(fullhouse(sevencards1))
print(fullhouse(sevencards2))
print(fullhouse(sevencards3))
print(fullhouse(sevencards4))
'''
def foak(sc):
	x = 0
	bin = []
	while x < len(sc):
		if sc[x][0] not in bin:
			bin.append(sc[x][0])
		x += 1
	counts = [0]*len(bin)
	x = 0
	while x < len(sc):
		if sc[x][0] in bin:
			counts[bin.index(sc[x][0])] += 1
		x += 1
	#print(counts)
	return counts.count(4)==1
'''
print(highcard(sevencards1))
print(highcard(sevencards2))

print(pair(sevencards1))
print(pair(sevencards2))

print(twopair(sevencards1))
print(twopair(sevencards2))
print("TOAK")
print(toak(sevencards1))
print(toak(sevencards2))

print(foak(sevencards1))
print(foak(sevencards2))
print(foak(sevencards3))
'''
sevencards4 = ["2S","3D","4H","5C","AS","2H", "6H"] # sample for testing
def straight(sc):
	# first order the cards
	order = "A23456789TJQKA"
	orderedRanks = ""
	for r in order:
		for c in sc:
			if c[0] in orderedRanks:
				pass
			elif c[0] == r:
				orderedRanks += r
	# now find if there are five consequetive ranks
	count = 0
	hit = False
	topOfStraight = "NO STRAIGHT"
	idx = 0
	validStraight = ""
	out = "-NOSTRAIGHT-"
	for r in order:
		if r == "J":
			break
		else:
			for x in range(0,5):
				validStraight +=  order[idx + x]
			idx += 1
		if validStraight in orderedRanks:
			out = validStraight
		validStraight = ""
	return out
'''
print(straight(sevencards4))
print(straight(sevencards1))
print(straight(sevencards2))
sevencards5 = ["2S","3S","4H","5S","AS","2H", "6S"]
sevencards6 = ["TS","JS","2H","8S","9S","4H","5S"]
sevencards7 = ["TS","JS","3S","8S","9S","2S","4S"]
sevencards8 = ["TS","JS","3S","8S","9S","4H","4S"]
'''
def flush(sc):
	suits = "DCHS"
	count = 0
	suit = ""
	found = ""
	put = False
	for s in suits:
		if count >= 5:
			break
		count = 0
		for c in sc:
			if c[1] == s:
				count += 1
				if count >= 5:
					suit = s
					#print(suit)
					pass
	out = count >= 5
	# now order the found cards
	order = "23456789TJQKA"
	#print(found)
	foundOrdered = []
	#print(sc)
	for o in order:
		for c in sc:
			if c[0] == o and c[1] == suit:
				foundOrdered.append(c)
	if count >= 5:
		#print(foundOrdered)
		out = [foundOrdered[-1], foundOrdered[-2], foundOrdered[-3], foundOrdered[-4], foundOrdered[-5]]
		#print(out)
	# give the flush a numeric score to compare it with other flushes
	score = 0
	vals = ["2","3","4","5","6","7","8","9","T","J","Q","K","A"]
	if count >= 5:
		for f in out: # making this OUT rather than foundOrdered means it doesn't count redundant cards in the score
			score += vals.index(f[0]) + 1
	return [out, score]
'''
print(flush(sevencards4))
print(flush(sevencards1))
print(flush(sevencards5))
print(flush(sevencards6))
print(flush(sevencards7))
print(flush(sevencards8))
'''
def strFlush(sc):
	out = False
	flushcards = flush(sc)
	strCards = straight(sc)
	strflCount = 0
	idx = 0
	strfl = ""
	if flushcards[1] != 0:
		#print("There is a flush")
		# now if there is a flush and also a straight flush, the suit of the flush
		# must also be the suit of the straight flush, because you cannot have two
		# flushes in one hand
		theSuit = flushcards[0][0][1]
		#print(theSuit)
		
		if len(strCards) == 5:
			#print("There is a straight")
			for x in ["A2345", "23456", "34567", "45678", "56789", "6789T", "789TJ", "89TJQ", "9TJQK", "TJQKA"]:
				for y in x:
					if (y + theSuit) in sc:
						strflCount += 1
				if strflCount == 5:
					strfl = x
				strflCount  = 0
	if len(strfl) == 5:
		out = [True, strfl]
	return out
'''
sevencards9 = ["2S","2D","6H","7H","8H","9H","TH"]
sevencards10 = ["2S","JH","6H","7H","8H","9H","TH"]
sevencards11 = ["2S","JH","6H","7H","8H","9H","TD"]
print(strFlush(sevencards9)) # yes
print(strFlush(sevencards1)) # no
print(strFlush(sevencards10)) # yes
print(strFlush(sevencards11)) # no
'''	
'''

# now im just copying the code for straight with some changes 
	# first order the cards
	order = "A23456789TJQKA"
	orderedRanks = ""
	for r in order:
		for c in sc:
			if c[0] in orderedRanks:
				pass
			elif c[0] == r:
				orderedRanks += r
	outCards = []
	card = ""
	highest = ""
	if out:
		suit = flushcards[0][0][1]
		count = 0
		hits = 0
		for r in order:
			if r == "J":
				break
			for x in range(0,5):
				#print(order[count + x], end= "")
				if (order[count + x] + suit) in sc:
					#print("HIT", end="\t")
					hit += 1
					if hit == 5:
						highest = (order[count + x] + suit)
			count += 1
			hit = 0
		#print(highest)
	#print("OUTCARDS" + str(outCards))
	if out:
		out = highest
	else:
		out = "-NO STRAIGHT FLUSH-"
'''
