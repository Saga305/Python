print ("Enter number of instance for list:")
c = int(input());
print ("Enter the values for {} list  instance".format(c))
l = []

while c:
	i = input();
	c -= 1
	try:
		x = int(i)
		print ("this number is an int")
		l.append(x)
		continue
	except ValueError:
		pass
	try:
		x = float(i)
		print ("this number is a float")
		l.append(x)
		continue
	except ValueError:
		pass
	l.append(i)

print (l);
