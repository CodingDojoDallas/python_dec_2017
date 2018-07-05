def dictionaries(d): 
	for key, value in d.iteritems():
		print "My " + key + " is " + value + "."

dictionaries({"name": "Chris", "age": "42", "country of birth": "Germany", "favorite language": "CSS"})
