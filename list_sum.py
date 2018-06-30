lst =[ [1,2,3] , [1,2,9] , [9] , [9,9,9] , [1,2,3,9,9] ]

for l in lst: 
	print ("Input :" , l)
	ln = len(l) - 1
	if l[ln] < 9:
		l[ln] += 1
	else:
		while ln >= 0:
			if l[ln] == 9:
				l[ln] = 0
			else:
				l[ln] += 1
			ln -= 1
			if l[ln] != 9 and ln != -1:
				l[ln] += 1
				break
		if(ln < 0):
			l.insert(0,1)

	print("Output :" , l)
	print("========================")

"""
Testings:

Input : [1, 2, 3]
Output : [1, 2, 4]
========================
Input : [1, 2, 9]
Output : [1, 3, 0]
========================
Input : [9]
Output : [1, 0]
========================
Input : [9, 9, 9]
Output : [1, 0, 0, 0]
========================
Input : [1, 2, 3, 9, 9]
Output : [1, 2, 4, 0, 0]
========================
"""
