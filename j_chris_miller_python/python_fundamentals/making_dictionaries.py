Gname = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"]
Gfavorite_animal = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas"]

def making_dictionaries(name, favorite_animal):
	my_dict = dict(zip(name, favorite_animal))
	print my_dict

making_dictionaries(Gname, Gfavorite_animal)