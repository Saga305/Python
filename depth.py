#Find depth of given number in nested list.
print ("Enter list:")
l = [x for x in list(input()) if x != ',']
print ("Enter number:")
v = int(input())
st="l["
c = 0
ob = 0
cb = 0
for x in l:
	if x == '[':
		if c != 0:
			st = st + str(c-1)  + ']'
			st = st + '['
		c = 0
	elif x == ']':
		print ("Key is not present into nested list")
		break
	elif v == int(x):
		st = st +'[' + str(c-1)  + ']'
		print ("Depth of entered number is {} ".format(st))
		break
	c = c + 1



'''
Test 1:
	Enter list:
	[1,2,[3,4,[5,6,[7,8]]]
	Enter number:
	8
	Depth of entered number is l[2][2][2][1]


Test 2:
	Enter list:
	[1,2,[3,4,[5,6,[7,8]]]
	Enter number:
	1
	Depth of entered number is l[0] 

Test 3:
	Enter list:
	[1,2,[3,4,[5,6,[7,8]]]
	Enter number:
	5
	Depth of entered number is l[2][2][0] 

Test 4:
	Enter list:
	[1,2,3,[4,5,6]]
	Enter number:
	7
	Key is not present into nested list

''' 
