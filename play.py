import cards
import analyze07032026 as determine
import heuristic as heur
import random

deck = cards.deck

totalplayers = 6

balances = [200]* totalplayers

players = []
def printcards(cards, show):
	if not show:
		print(len(cards)*["X"])
	else:
		print(cards)
def getcards(deck, playernumber):
	x = [deck[(playernumber-1)*2], deck[(playernumber-1)*2 + 1]]
	#print(x[0] + ", " + x[1])
	return x
showpcards = True
dealer = 1

def decide(cards):
	out = ""
	score = heur.simplestheur(cards)
	decider = random.randint(10,88)
	if decider > score + 20:
		out = "FOLD"
	elif decider < score - 20:
		out = "RAISE"
	else:
		out = "CALL"
	return out
# game decision string
def dformat(playernum, cards):
	decision = decide(cards)
	out = "Player " + str(playernum) + ": " + decision
	print(out)
	return decision

moddy = totalplayers + 1 # regularly used to help rotate players

def incpnum(pnum, folded):
	global moddy
	playernum = (pnum + 1) % moddy
	if playernum == 0:
		playernum = 1
	while playernum in folded:
		playernum = (playernum + 1) % moddy
		if playernum == 0:
			playernum = 1
		if len(folded) == moddy - 1:
			playernum = -1
		#print("HERE")
		#print(playernum)
		#input("")
	return playernum
# amount can be plus or minus, balances and pot must be lists
def changebal(balances, playernum, amount, pot):
	balances[playernum - 1] += amount
	pot[0] -= amount
def conseq(playernum, decision, raisetally, balances, pot, folded, lasttocall, smallblind):
	dec = decision
	callamount = 0
	raiseamount = 0
	# for if you can't raise as much as the raisetally due to balance
	if dec == "RAISE" and balances[playernum-1] < raisetally[0]:
		dec = "CALL"
		raiseamount = balances[playernum-1]
	if dec == "RAISE":
	
		raisetally[0] += 2
		raiseamount = -raisetally[0]
		if smallblind[0] == playernum:
			smallblind[0] = "None"
			raiseamount += 1
		if raiseamount > balances[playernum-1]:
			dec = "CALL"
			callamount = balances[playernum -1]
		changebal(balances, playernum, raiseamount, pot)
		lasttocall[0] = playernum - 1
		if lasttocall[0] == 0:
			lasttocall[0] = 6
		while lasttocall[0] in folded:
			lasttocall[0] = (lasttocall[0] - 1)
			if lasttocall[0] == 0:
				lasttocall[0] = 6
	if dec == "CALL":
		am = -raisetally[0]
		if playernum == smallblind[0]:
			smallblind[0] = "None"
			am = am + 1
		if callamount != 0: # this fires if he wanted to raise but can't
			am = callamount
		changebal(balances, playernum, am, pot)
		if playernum == lasttocall[0]:
			lasttocall = ["done"]
	elif dec == "FOLD":
		folded.append(playernum)
		if playernum == lasttocall[0]:
			lasttocall = ["done"]
round_ = 1
folded = []
dealer = 1
choicesmade = 0
## GAME LOOP ##
while True:
	if round_ == 4:
		break
	print(" --- ROUND "+ str(round_) + " ---")
	if round_ == 1:
		lasttocall = [3]
		lasttocheck = [3]
		playernum = 2
		folded = [] # list of playernumbers who have folded
		pot = [0]
		raisetally = [2] # helps log reraises
		smallblind = 0 # if he calls or raises i need to modify it
		# reset dealer chip if player limit reached
		if dealer == totalplayers:
			dealer = 1
		allplayablecards = cards.getnew(totalplayers*2 + 5)
		for i in range(0,totalplayers):
			print(str(i + 2) + ": ", end="")
			players.append(getcards(allplayablecards, i + 2))
			printcards(players[i], showpcards)
		table = [allplayablecards[-1],allplayablecards[-2],allplayablecards[-3],allplayablecards[-4],allplayablecards[-5]]
		flop = table[0:3]
		#print(players)
		print(table)
		input("")
		## BLINDS ##
		print("Player " + str(playernum) + " SMALL BLIND")
		smallblind = [playernum]
		changebal(balances, playernum, -1, pot)
		playernum = incpnum(playernum, folded)
		
		print("Player " + str(playernum) + " BIG BLIND")
		changebal(balances, playernum, -2, pot)
		playernum = incpnum(playernum, folded)
		## START OF BETTING OUTSIDE OF BLINDS
		while lasttocall[0] != "done" and playernum != -1:
			if playernum not in folded:
				d = dformat(playernum, players[playernum-1] + flop) # this function makes the decision of the player
				if d == "RAISE":
					lasttocheck[0] = -1 ## nullify
				if (d == "CALL" or d == "FOLD") and playernum == lasttocheck[0]:
					if d == "FOLD":
						folded.append(playernum)
					print("---ROUND OVER---")
					round_ = 2
					print("---POT IS " + str(pot[0]) + "---")
					ingame = [] # helps with debugging
					for x in [1,2,3,4,5,6]:
						if x not in folded:
							ingame.append(x)
					print("PLAYERS IN THE GAME ARE: " + str(ingame) + "")
					if len(ingame) == 1:
						round_ = 4 ## all rounds over
					break
				if lasttocall[0] == playernum and d == "CALL":
					print("---ROUND OVER---")
					round_ = 2
					print("---POT IS " + str(pot[0]) + "---")
					ingame = [] # helps with debugging
					for x in [1,2,3,4,5,6]:
						if x not in folded:
							ingame.append(x)
					print("PLAYERS IN THE GAME ARE: " + str(ingame) + "")
					if len(ingame) == 1:
						round_ = 4 ## all rounds over
					break
				if lasttocall[0] == playernum and d == "FOLD":
					print("---ROUND OVER---")
					round_ = 2
					print("---POT IS " + str(pot[0]) + "---")
					ingame = [] # helps with debugging
					for x in [1,2,3,4,5,6]:
						if x not in folded and x != playernum:
							ingame.append(x)
					print("PLAYERS IN THE GAME ARE: " + str(ingame) + "")
					if len(ingame) == 1:
						round_ = 4 ## all rounds over
					break
				
				conseq(playernum, d, raisetally, balances, pot, folded, lasttocall, smallblind)
				print("POT: " + str(pot[0]))
				print("LAST TO CALL: " + str(lasttocall[0]))
				playernum = incpnum(playernum, folded)
				#print("FOLD BIN: " + str(folded))
				ingame = [] # helps with debugging
				for x in [1,2,3,4,5,6]:
					if x not in folded:
						ingame.append(x)
				if len(ingame) == 1:
					print("---ROUNDs OVER--- player " + str(ingame[0]) + " wins " + str(pot[0]))
					round_ = 4
					break
				#print(lasttocall)
				input("")
		round_ =2
	else:
		raisetally = [2] 
		if round_ == 4:
			print("---ROUNDS OVER---")
			break
		tablecards = []
		smallblind[0] = -1 # not needed here
		if round_ == 2:
			tablecards = table[0:4]
		elif round_ == 3:
			tablecards = table[0:5]
		lasttocall = [dealer]
		lasttocheck = [dealer]
		print(str(lasttocheck))
		while lasttocheck[0] in folded:
			lasttocheck[0] -= 1
			if lasttocheck[0] == 0:
				lasttocheck[0] = 6
		while lasttocall[0] in folded:
			lasttocall[0] -= 1
			if lasttocall[0] == 0:
				lasttocall[0] = 6
		pplist = [2,3,4,5,6, 1] # potential players list, in order of play
		playernum - 2
		for p in pplist:
			if p not in folded:
				playernum = p
				break
		## START OF BETTING
		while lasttocall[0] != "done" and playernum != -1:
			if playernum not in folded:
				d = dformat(playernum, players[playernum-1] + tablecards) # this function makes the decision of the player
				if d == "RAISE":
					lasttocheck[0] = -1 ## nullify
				if (d == "CALL" or d == "FOLD") and playernum == lasttocheck[0]:
					print("section a")
					if d == "FOLD":
						folded.append(playernum)
					print("---ROUND OVER---")
					print("---POT IS " + str(pot[0]) + "---")
					ingame = [] # helps with debugging
					for x in [1,2,3,4,5,6]:
						if x not in folded:
							ingame.append(x)
					print("PLAYERS IN THE GAME ARE: " + str(ingame) + "")
					break
				if lasttocall[0] == playernum and d == "CALL":
					print("section b")
					print("---ROUND OVER---")
					print("---POT IS " + str(pot[0]) + "---")
					ingame = [] # helps with debugging
					for x in [1,2,3,4,5,6]:
						if x not in folded:
							ingame.append(x)
					print("PLAYERS IN THE GAME ARE: " + str(ingame) + "")
					break
				if lasttocall[0] == playernum and d == "FOLD":
					print("section c")
					if d == "FOLD":
						folded.append(playernum)
					print("---ROUND OVER---")
					print("---POT IS " + str(pot[0]) + "---")
					ingame = [] # helps with debugging
					for x in [1,2,3,4,5,6]:
						if x not in folded and x != playernum:
							ingame.append(x)
					print("PLAYERS IN THE GAME ARE: " + str(ingame) + "")
					break
				# need to add folded player if he wasn't already added:
				if d == "FOLD" and playernum not in folded:
					folded.append(playernum)
				conseq(playernum, d, raisetally, balances, pot, folded, lasttocall, smallblind)
				print("POT: " + str(pot[0]))
				print("LAST TO CALL: " + str(lasttocall[0]))
				playernum = incpnum(playernum, folded)
				#print("FOLD BIN: " + str(folded))
				ingame = [] # helps with debugging
				for x in [1,2,3,4,5,6]:
					if x not in folded:
						ingame.append(x)
				if len(ingame) == 1:
					print("---ROUND OVER--- player " + str(ingame[0]) + " wins " + str(pot[0]))
					break
				#print(lasttocall)
				input("")
			else:
				playernum = incpnum(playernum, folded)
		round_ += 1
