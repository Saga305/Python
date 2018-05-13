#Get the binary number from user and check the divisibilty by 2.
print ("Enter binary number")
s= input()
if(int(s,2)%2 == 0):
	print ("{} [Desimal:{}] is divisible by 2".format(s,int(s,2)))
else:
	print ("{} [Desimal:{}] is not divisible by 2".format(s,int(s,2)))
