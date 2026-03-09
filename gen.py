import analyze07032026
import cards

sc = cards.deck[0:7]

def generate():
	global sc
	x8 = False
	while not x8:
		sc = cards.shuffle120(cards.deck)[0:7]
		print(sc)
		x8 = analyze07032026.strFlush(sc) # True
		x7 = analyze07032026.foak(sc) # True
		x6 = analyze07032026.fullhouse(sc) # [0] == True
		x5 = analyze07032026.flush(sc) # [0] == True
		x4 = analyze07032026.straight(sc) # len() == 5
		x3 = analyze07032026.toak(sc) # True
		x2 = analyze07032026.twopair(sc) # [0] == True
		x1 = analyze07032026.pair(sc) # [0] == 1
		if x8:
			print("STRAIGHT FLUSH")
			pass
		elif x7:
			print("FOUR OF A KIND")
			pass
		elif x6[0]:
			print("FULL HOUSE")
			pass
		elif x5[0]:
			print("FLUSH")
			pass
		elif len(x4)==5:
			print("STRAIGHT")
			pass
		elif x3:
			print("THREE OF A KIND")
			pass
		elif x2:
			print("TWO PAIR")
			pass
		elif x1[0]==1:
			print("PAIR")
			pass
		else:
			print("HIGH CARD")
		#input("")
generate()
