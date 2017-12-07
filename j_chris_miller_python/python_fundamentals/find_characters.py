# input
word_list = ['hello','world','my','name','is','Anna']
char = 'o'
full_string = ""

for i in range(0, len(word_list)):
	# if word_list[i].find(char) != -1:
	if char in word_list[i]:
		full_string += word_list[i]

print full_string

