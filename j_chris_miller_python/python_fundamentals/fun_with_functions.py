#fun_with_functions
#Odd/Even
def odd_even():
	for i in range(2001):
		print "Number is " + str(i)
		if (i % 2 == 0):
			print "This is an even number"
		else:
			print "This is an odd number"

odd_even()

#Multiply
def multiply(arr):
	for i in range(len(arr)):
		arr[i] *= 5
	return arr

multiply([2, 3, 5, 2, 7])

#Hacker Challenge
def layered_multiples(arr):
	print arr
	new_arr = []
	for i in arr:
		val_arr = []
		for i in range (x):
			val_arr.append(1)
		new_array.append(val_arr)
	return new_array

i = layered_multiples(multiply([2,4,5],3))
print i


