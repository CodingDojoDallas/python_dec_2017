#Multiples

for num in range(1,1001):
	if (num %2 !=0):
		print num

for num in range(1,1001):
	if (num %5 == 0):
		print num

#Sum List

a = [1,2,5,10,255,3]

print sum(a)

list_sum = sum(a)
list_avg = list_sum/len(a)

print list_avg