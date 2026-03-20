def a(b):
	d = []
	d = b.copy()
	d = [1,2]
	b = d
c = [100,1000]
a(c)
if c == [100,1000]:
	print("function dont mutate lists")
else:
	print("functions mutate lists")

import cards
x = cards.deck
print(x)
