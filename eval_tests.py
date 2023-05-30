import HandEval as h
tableCards = ["AS", "KD", "2D", "QS", "7H"]
handCards = ["AD", "9C"]
ranks = ["HIGH CARD", "PAIR", "TWO PAIR", "THREE OF A KIND", "STRAIGHT", "FLUSH", "FULL HOUSE", "FOUR OF A KIND", "STRAIGHT FLUSH", "ROYAL FLUSH"]
def testPair():
	tableCards = ["AS", "KD", "2D", "QS", "7H"]
	handCards = ["AD", "9C"]
	assert(h.pair(tableCards, handCards))
	print("Pair is detected")
	tableCards = ["AS", "KD", "2D", "QS", "7H"]
	handCards = ["JD", "9C"]
	assert(not h.pair(tableCards, handCards))
	tableCards = ["AS", "AD", "2D", "QS", "7H"]
	handCards = ["JD", "AC"]
	assert(not h.pair(tableCards, handCards))
	tableCards = ["AS", "AD", "2D", "QS", "7H"]
	handCards = ["JD", "2C"]
	assert(not h.pair(tableCards, handCards))
	print("Pair is not falsely detected")
testPair()
def testTOAK():
	tableCards = ["AS", "KD", "2D", "AH", "7H"]
	handCards = ["AD", "9C"]
	assert(h.toak(tableCards, handCards, 3)>=1)
	print("TOAK is detected")
	tableCards = ["AS", "KD", "2D", "QS", "7H"]
	handCards = ["JD", "9C"]
	assert(not h.toak(tableCards, handCards, 3)>=1)
	tableCards = ["AS", "AD", "9D", "QS", "7H"]
	handCards = ["JD", "9C"]
	assert(not h.toak(tableCards, handCards, 3)>=1)
	print("TOAK is not falsely detected")
	tableCards = ["AS", "AD", "9D", "JS", "JH"]
	handCards = ["JD", "AC"]
	assert(h.toak(tableCards, handCards, 3)>=1)
	print("Two TOAK count")
testTOAK()
def testFOAK():
	tableCards = ["AS", "KD", "2D", "AH", "7H"]
	handCards = ["AD", "AC"]
	assert(h.toak(tableCards, handCards, 4)==1)
	print("FOAK is detected")
	tableCards = ["AS", "KD", "2D", "QS", "7H"]
	handCards = ["JD", "9C"]
	assert(not h.toak(tableCards, handCards, 4)==1)
	tableCards = ["AS", "KD", "2D", "AS", "7H"]
	handCards = ["KS", "AC"]
	assert(not h.toak(tableCards, handCards, 4)==1)
	print("FOAK is not falsely detected")
testFOAK()
def testStraight():
	tableCards = ["AS", "2D", "3D", "AH", "7H"]
	handCards = ["4D", "5C"]
	assert(h.straight(tableCards, handCards))
	print("Straight is detected")
	tableCards = ["KS", "2D", "3D", "AH", "7H"]
	handCards = ["4D", "5C"]
	assert(h.straight(tableCards, handCards))
	print("Straight is not falsely detected")
testStraight()
def testFlush():
	tableCards = ["AS", "2S", "3S", "AH", "7S"]
	handCards = ["4D", "5S"]
	assert(h.flush(tableCards, handCards))
	print("Flush is detected")
	tableCards = ["KS", "2D", "3D", "AH", "7H"]
	handCards = ["4D", "5C"]
	assert(not h.flush(tableCards, handCards))
	print("Flush is not falsely detected")
testFlush()
def testStrFlush():
	tableCards = ["JS", "2S", "3S", "4S", "QD"]
	handCards = ["6S", "5S"]
	assert(h.strFlush(tableCards, handCards))
	print("Straight-flush is detected")
	tableCards = ["JS", "2S", "AS", "4S", "QD"]
	handCards = ["6S", "5S"]
	assert(not h.strFlush(tableCards, handCards))
	tableCards = ["AD", "2S", "3S", "4D", "QD"]
	handCards = ["9S", "5S"] # straight no flush
	assert(not h.strFlush(tableCards, handCards))
	tableCards = ["AS", "3S", "KS", "AH", "AD"]
	handCards = ["6S", "7S"] # flush no straight
	assert(not h.strFlush(tableCards, handCards))
	tableCards = ["AS", "2S", "3S", "4H", "AD"]
	handCards = ["5S", "TS"] # flush and straight but no straight-flush
	assert(not h.strFlush(tableCards, handCards))
	print("Straight-flush is not falsely detected")
testStrFlush()
def testFH():
	tableCards = ["JS", "JD", "QS", "4S", "5D"]
	handCards = ["QD", "JH"]
	assert(h.fh(tableCards, handCards))
	tableCards = ["JS", "JD", "QS", "QH", "5D"]
	handCards = ["QD", "JH"]
	assert(h.fh(tableCards, handCards))
	print("Full-house is detected")
	tableCards = ["JS", "JD", "QS", "QH", "5D"]
	handCards = ["JH", "JC"]
	assert(not h.fh(tableCards, handCards))
	print("Full-house is not falsely detected")
testFH()
import basics as b
def testDetermine():
	d = b.deck
	tableCards = [d[0], d[1], d[2], d[3], d[4]]
	handCards = [d[5], d[6]]
	print(tableCards + handCards, end=": ")
	h.determine(tableCards, handCards)
testDetermine()
