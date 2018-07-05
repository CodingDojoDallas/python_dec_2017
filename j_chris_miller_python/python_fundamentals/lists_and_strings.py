# • .find()
 
# • .replace()
 
# • min()
 
# • max()
 
# • .sort()
 
# • len()
 
words = "It's thanksgiving day. It's my birthday,too!"
 
print(words.find("day"))
 
print(words.replace("day", "month"))
 
x = [2,54,-2,7,12,98]
 
#print(x.min(), x.max())
print (min(x), max(x))
x = ["hello",2,54,-2,7,12,98,"world"]
 
print( x[0], x[-1] )
 
#y =x[0]
#z =x[-1]
#arr=[y,z]
arr=[ x[0],x[-1] ]
print(arr)
 
#Start with a list like this one: x = [19,2,54,-2,7,12,98,32,10,-3,6]. Sort your list first. Then, split your list in half. Push the list created from the first half to position 0 of the list created from the second half. The output should be: [[-3, -2, 2, 6, 7], 10, 12, 19, 32, 54, 98]. Stick with it, this one is tough!
 
 
x = [19,2,54,-2,7,12,98,32,10,-3,6]
 
x.sort()
 
print(x)
 
y=int(len(x)/2)
 
x[:y]
 
print(x[:y])
 
front = x[:y]
 
back = x[y:]
 
back.insert(0,front)
 
print (back)