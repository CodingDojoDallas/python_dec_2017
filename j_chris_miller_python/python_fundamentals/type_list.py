arr = [8, "9",9, "7"]
sum = 0
full_string = ""
for i in range(len(arr)):
	if (type(arr[i]) == int):
		for j in range(len(arr)):
			if (type(arr[j]) == str):
				print "mixed"
				break
		sum += arr[i]
	elif (type(arr[i]) == str):
		full_string += arr[i]




print sum, full_string