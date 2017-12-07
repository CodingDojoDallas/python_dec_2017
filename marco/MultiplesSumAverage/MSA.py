for count in range(1, 1000):
	if count % 2==1:
		print count

for count in range(5, 1000001):
	if count % 5==0:
		print count

a=[1,2,5,10,255,3]
sum=0
for i in a:
	sum+= i
print sum

print sum/len(a)