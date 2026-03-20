# the purpose of this file is to give a way or ways for the non human players to make intelligent decisions

import analyze07032026 as z

ranks = ["2","3","4","5","6","7","8","9","T","J","Q","K","A"]

def preflop(c1, c2):
	pocketpair = c1[0] == c2[0]
	global ranks
	strength1 = ranks.index(c1[0]) + 1
	strength2 = ranks.index(c2[0]) + 1
	suited = c1[1] == c2[1]
	
	score = suited*10 + pocketpair*10*strength1 + strength1*5 + strength2*5
	
	return score

def tfStraight(sc):
	ra = []
	for c in sc:
		ra.append(c[0])
	#print(ra)
	cond3 = False
	# sort by rank and remove duplicates
	r = "AKQJT98765432"
	out = ""
	for x in r:
		if x in ra:
			out += x
	sortedRanks = out
	#print(sortedRanks)
	idx = 0
	cand = ""
	score = 0
	avail = ["A5432", "65432", "76543","87654", "98765","T9876", "JT987", "QJT98", "KQJT9", "AKQJT"]
	while idx <= len(sortedRanks) - 5:
		cand = sortedRanks[idx:idx + 5]
		if cand in avail:
			cond3 = True # if there's a straight
			#print(cand)
			score = avail.index(cand) + 1
		idx += 1
	return [cond3, score]
def scores(cards):
	pair = z.pair(cards)[0] == 1
	twopair = z.twopair(cards)[0] == 1
	toak = z.toak(cards)[0]
	straight = tfStraight(cards)[0] == 1
	flush = z.flush(cards)[0]
	fh = z.fullhouse(cards)[0]
	foak = z.foak(cards)[0]
	sf = z.strFlush(cards)[0]
	return [pair, twopair, toak, straight, flush, fh, foak, sf]
'''
postflop(["2H", "2D", "4C", "6H", "8D"])
postflop(["2H", "2D", "3D", "3H", "5C"])
postflop(["2H", "2C", "2D", "5D", "7D"])
postflop(["2H", "3D", "4D", "5D", "6D"])
postflop(["2D", "3D", "4D", "5D", "7D"])
postflop(["2S", "2D", "2C", "3H", "3S"])
postflop(["2D", "3D", "4D", "5D", "6D"])
'''
scores(["2D", "2H", "2C", "2S", "3D"])

# 1 = high card. 2 - pair...
def mainscore(cards):
	i = 0
	score = 0
	vals = scores(cards)
	#print(vals)
	while i < 8:
		if vals[i] == True:
			score = i + 1
		i += 1
	if score == 0:
		i = 1
	return score
# score within mainscore
def subscore(cards):
	val = mainscore(cards)
	pair = z.pair(cards)[1]
	twopair = z.twopair(cards)[1]
	toak = z.toak(cards)[1]
	straight = z.straight(cards)[1]
	flush = z.flush(cards)[1]
	fh = z.fullhouse(cards)[1]
	foak = z.foak(cards)[1]
	sf = z.strFlush(cards)[1]
	highcard = 0
	if not pair and not twopair and not toak and not straight and not flush and not fh and not foak and not sf:
		highcard = z.score(cards)
	subscore = 0
	for x in [highcard, pair, twopair, toak, straight, flush, fh, foak, sf]:
		if len(str(x)) > 0 and x != 0:
			subscore = x
	return subscore
'''
subscore(["2H", "AD", "4C", "6H", "8D"])
subscore(["2H", "2D", "4C", "6H", "8D"])
subscore(["2H", "2D", "3D", "3H", "5C"])
subscore(["2H", "2C", "2D", "5D", "7D"])
subscore(["2H", "3D", "4D", "5D", "6D"])
subscore(["2D", "3D", "4D", "5D", "7D"])
subscore(["2S", "2D", "2C", "3H", "3S"])
subscore(["2D", "2H", "2C", "2S", "3D"])
subscore(["2D", "3D", "4D", "5D", "6D"])
'''
def decision(cards):
	x = mainscore(cards)
	#print(x)
	highcardonly = x==1
	if highcardonly:
		return "CHECK OR FOLD"
#print(decision(["2H", "AD", "4C", "6H", "8D"]))

def compscore(pc, tablecards):
	s1 = mainscore(pc + tablecards)
	s2 = subscore(pc + tablecards)
	out = s1 + s2/(10**len(str(s2)))
	print(out)
	print("\t" + str(s2))
	return out
'''
pc = ["3C", "7H"]
compscore(pc, ["2H", "AD", "4C", "6H", "8D"])
pc = ["2C", "7H"]
compscore(pc, ["2H", "AD", "4C", "6H", "8D"])
compscore(pc, ["2H", "2D", "4C", "6H", "8D"])
compscore(pc, ["2H", "2D", "3D", "3H", "5C"])
compscore(pc, ["2H", "2C", "2D", "5D", "7D"])
compscore(pc, ["2H", "3D", "4D", "5D", "6D"])
compscore(pc, ["2D", "3D", "4D", "5D", "7D"])
pc = ["8C", "7H"]
compscore(pc, ["2S", "2D", "2C", "3H", "3S"])
compscore(pc, ["2D", "2H", "2C", "2S", "3D"])
compscore(pc, ["2D", "3D", "4D", "5D", "6D"])
'''
# top limit = 88, bottom limit = 10
def simplestheur(sc):
	ranks = ["2","3","4","5","6","7","8","9","T","J","Q","K","A"]
	sizetotal = 0
	for c in sc:
		sizetotal += ranks.index(c[0]) + 1
	#print(sizetotal)
	return sizetotal
'''
pc = ["AS", "AH"]
simplestheur(pc + ["AC", "AD", "KS", "KH", "KD"])
pc = ["2S", "2H"]
simplestheur(pc + ["2C", "2D", "3S", "3H", "3D"])
'''
