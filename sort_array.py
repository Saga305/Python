"""
Sort all odd numbers from given list without chnaging the order of even number.
Note: consider 0 as even number.

Input list:	 [5, 3, 2, 8, 1, 4, 0, 0, 1, 2, 3]
Output list:	 [1, 1, 2, 8, 3, 4, 0, 0, 3, 2, 5]

"""

lst = [5,3,2,8,1,4,0,0,1,2,3]
l = [x for x in lst if (x != 0 and  x%2!=0)]
l.sort()
l.reverse()
print ("Input list:\t",lst)

cnt = 0
for i in lst:
	if (i != 0 and i%2!=0):
		lst[cnt] = l.pop()
	cnt = cnt + 1
	
print ("Output list:\t",lst)
