#Write a programe to check divisibilty of each digit of the number by 2 for given range of number.
def check_divisibility_by_2(num):
	l = [int(x) for x in str(num) if (int(x)%2) == 0]
	if len(l) == len(str(num)):
		print (num)
	
for x in range (2000,3000):
	check_divisibility_by_2(x)
