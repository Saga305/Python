def remove_duplicate(l):
	count = 0
	for i in l:
		#if i.startswith(i[0]) and i.endswith(i[0]):
		if i[0] == i[-1]:
			count += 1
	return count


l=['abc', 'zaz', 'aba', "AjA"]
print (remove_duplicate(l))

