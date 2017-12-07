
x = [4, 6, 1, 3, 5, 7, 25]
def draw_stars(x):
	star ="*"
	for i in x:
		print star * i


draw_stars(x)


x = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]
def factory(x):
	star = '*'
	for i in x:
		if type(i) is int:
			print star * i
		elif type(i) is str:
			print i[0].lower()*len(i)



factory(x)