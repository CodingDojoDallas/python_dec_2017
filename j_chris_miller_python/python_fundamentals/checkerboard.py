for i in range(0,4):	
	check = ""
	board = ""
	#for i in range (0,4):
	for i in range(0,8):
		if (i % 2 != 0):
			check += " "
		else:
			check += "*"
	print check
	for i in range(0,8):
		if (i % 2 != 0):
			board += "*"
		else:
			board += " "
	print board
