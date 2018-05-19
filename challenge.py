#Reverse string by word.
def rev_by_word(str):
	l = []
	l2 = []
	s=""
	for i in str:
		if(i.isalpha()):
			s = s+i
		else:
			l2.append(i)
			l.append(s)
			s=""
	n = len(l) -1
	i = 0
	while(n > -1):
		s +=  l[n]
		s +=  l2[i]
		n -= 1
		i += 1
	return s

str= "Welcome#to@my2class!"
print (rev_by_word(str))

