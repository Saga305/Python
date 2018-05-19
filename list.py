def remove_duplicate(l):
	l2= []
	for i in l:
		if l2.count(i) == 2:
			l2.append(i);
	return l2

l =[1,2,3,3,3,4,4,5,6,7]
print (remove_duplicate(l))
