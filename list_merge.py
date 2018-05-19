l = [1,2,3]
l1 = [4,5,6,1]

for i in l:
	if i in l1:
		l = l+l1
		break

print (l)	
