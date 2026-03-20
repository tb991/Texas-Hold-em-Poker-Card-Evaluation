import cards


import analyze07032026 as an

def isHighCard(sc):
	ranks = []
	for c in sc:
		ranks.append(c[0])
	cond1 = len(sc) == len(set(ranks)) # if all ranks are distinct
	
	suits = []
	for c in sc:
		suits.append(c[0])
	cond2 = False
	for s in "SHCD":
		if suits.count(s) >= 5:
			cond2 = True # if there's five or more of one suit
			break
	cond3 = False
	# sort by rank and remove duplicates
	r = "AKQJT98765432"
	out = ""
	for x in r:
		if x in ranks:
			out += x
	sortedRanks = out
	idx = 0
	cand = ""
	while idx < len(sortedRanks) - 5:
		cand = sortedRanks[idx:idx + 5]
		if cand in ["A5432", "AKQJT", "KQJT9", "QJT98", "JT987", "T9876", "98765", "87654", "76543", "65432"]:
			cond3 = True # if there's a straight
		idx += 1
	return cond1 and not cond2 and not cond3

count1 = 0
count2 = 0
total = 0

while total < 10000:
	nc = cards.getnew(9)

	sc1 = nc[0:7]
	sc2 = nc[2:9]


	p1hc = isHighCard(sc1)
	p2hc = isHighCard(sc2)

	if p1hc:
		count1 += 1
	if p2hc:
		count2 += 1
	total += 1
print("Player 1 high card rate: " + str(count1/total))
print("Player 2 high card rate: " + str(count2/total))
