import analyze07032026
import cards

sc = cards.deck[0:7]
sixSuit = False
def generate():
	global sc
	global sixSuit
	x5 = [False]
	hc = 0
	p = 0
	tp = 0
	tk = 0
	str_ = 0
	fl = 0
	fh = 0
	fk = 0
	sf = 0
	while hc < 100000:
		sc = cards.shuffle120(cards.deck)[0:7]
		'''
		fCount = 0
		sixSuit = False
		for x in "SHCD":
			for x1 in sc:
				if x1[1] == x:
					fCount += 1
					if fCount == 7:
						sixSuit = True
			fCount = 0
		'''
		#print(sc)
		x8 = analyze07032026.strFlush(sc) # True
		x7 = analyze07032026.foak(sc) # True
		x6 = analyze07032026.fullhouse(sc) # [0] == True
		x5 = analyze07032026.flush(sc) # [0] == True
		x4 = analyze07032026.straight(sc) # len() == 5
		x3 = analyze07032026.toak(sc) # True
		x2 = analyze07032026.twopair(sc) # [0] == True
		x1 = analyze07032026.pair(sc) # [0] == 1
		if x8:
			#print("STRAIGHT FLUSH")
			sf += 1
			pass
		elif x7:
			#print("FOUR OF A KIND")
			fk += 1
			pass
		elif x6[0]:
			#print("FULL HOUSE")
			fh += 1
			pass
		elif x5[0]:
			#print("FLUSH")
			fl += 1
			pass
		elif len(x4)==5:
			#print("STRAIGHT")
			str_ += 1
			pass
		elif x3:
			#print("THREE OF A KIND")
			tk += 1
			pass
		elif x2:
			#print("TWO PAIR")
			tp += 1
			pass
		elif x1[0]==1:
			#print("PAIR")
			p += 1
			pass
		else:
			#print("HIGH CARD")
			hc += 1
		#input("")
	s = hc + p + tp + tk + str_ + fl + fh + fk + sf
	print("HIGH CARD")
	print(str(hc) + "\t" + str(hc/s))
	print("PAIR")
	print(str(p)+ "\t" + str(p/s))
	print("TWO PAIR")
	print(str(tp)+ "\t" + str(tp/s))
	print("THREE OF A KIND")
	print(str(tk)+ "\t" + str(tk/s))
	print("STRAIGHT")
	print(str(str_)+ "\t" + str(str_/s))
	print("FLUSH")
	print(str(fl)+ "\t" + str(fl/s))
	print("FULL HOUSE")
	print(str(fh)+ "\t" + str(fh/s))
	print("FOUR OF A KIND")
	print(str(fk)+ "\t" + str(fk/s))
	print("STRAIGHT FLUSH")
	print(str(sf)+ "\t" + str(sf/s))
	
generate()
