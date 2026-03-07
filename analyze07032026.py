# purpose of this file is to look at 7 available cards and call relevant functions to check what the player has


sevencards1 = ["2S","2D","3H","3C","4S","4H", "4D"] # sample for testing
sevencards2 = ["2S","3D","5H","6C","AS","QH", "TH"] # sample for testing
sevencards3 = ["2S","2D","5H","2C","AS","2H", "TH"] # sample for testing

def highcard(sc):
	x = 0
	bin = []
	while x < len(sc):
		if sc[x][0] not in bin:
			bin.append(sc[x][0])
		x += 1
	return len(bin)

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
	print(counts)
	return counts.count(2)

def twopair(sc):
	out = ""
	if pair(sc) == 2:
		out = True
	else:
		out = False
	return out

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
	print(counts)
	return counts.count(3)==1 or counts.count(3)==2
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
	print(counts)
	return counts.count(4)==1

print(highcard(sevencards1))
print(highcard(sevencards2))

print(pair(sevencards1))
print(pair(sevencards2))

print(twopair(sevencards1))
print(twopair(sevencards2))

print(toak(sevencards1))
print(toak(sevencards2))

print(foak(sevencards1))
print(foak(sevencards2))
print(foak(sevencards3))

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
print(straight(sevencards4))
print(straight(sevencards1))
print(straight(sevencards2))
sevencards5 = ["2S","3S","4H","5S","AS","2H", "6S"]
sevencards6 = ["TS","JS","2H","8S","9S","4H","5S"]
sevencards7 = ["TS","JS","3S","8S","9S","2S","4S"]
sevencards8 = ["TS","JS","3S","8S","9S","4H","4S"]
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
	if count >= 5:
		for f in out: # making this OUT rather than foundOrdered means it doesn't count redundant cards in the score
			vals = ["2","3","4","5","6","7","8","9","T","J","Q","K","A"]
			score += vals.index(f[0])
	return [out, score]

print(flush(sevencards4))
print(flush(sevencards1))
print(flush(sevencards5))
print(flush(sevencards6))
print(flush(sevencards7))
print(flush(sevencards8))

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
sevencards9 = ["2S","2D","6H","7H","8H","9H","TH"]
sevencards10 = ["2S","JH","6H","7H","8H","9H","TH"]
sevencards11 = ["2S","JH","6H","7H","8H","9H","TD"]
print(strFlush(sevencards9)) # yes
print(strFlush(sevencards1)) # no
print(strFlush(sevencards10)) # yes
print(strFlush(sevencards11)) # no

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
