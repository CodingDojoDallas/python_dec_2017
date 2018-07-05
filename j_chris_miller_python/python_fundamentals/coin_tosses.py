#Coin Tosses
from random import *
def coin_toss():
	headcount = 0
	tailcount = 0
	count = 0
	for i in range(5000):
		num = randint(0,1)
		if num == 0:
			headcount = headcount + 1
			print "Attempt #" + str(count) + ": Throwing a coin... It's a head! ... Got " + str(headcount) + " heads so far and " + str(tailcount) + " tails so far"
		else:
			print "Attempt #" + str(count) + ": Throwing a coin... It's a tails! ... Got " + str(headcount) + " heads so far and " + str(tailcount) + " tails so far"
			tailcount = tailcount + 1
		count = count + 1
	ratio = float(tailcount)/headcount
	print str(ratio) + " equals the tails ratio"
		
coin_toss()