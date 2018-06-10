"""
Hello All,
Here i have written a code to store user input into dictonary value list and reoving duplicate Id's.

Test: 
Enter Id:1
Enter Name:amar 
Enter Age:23
Enter salary in LPA:3
Do you want to add one more entery YES or NO:y
Enter Id:2
Enter Name:akbar
Enter Age:30
Enter salary in LPA:5
Do you want to add one more entery YES or NO:y
Enter Id:1
Enter Name:anthony
Enter Age:35
Enter salary in LPA:10
Do you want to add one more entery YES or NO:y
Enter Id:4
Enter Name:motilal 
Enter Age:50
Enter salary in LPA:19
Do you want to add one more entery YES or NO:no
Your dictonary : {'Name': ['Amar', 'Akbar', 'Anthony', 'Motilal'], 'Salary': [3.0, 5.0, 10.0, 19.0], 'Age': [23, 30, 35, 50], 'Id': [1, 2, 1, 4]}
[1, 2, 4]
Dictnary after removing duplicate Id's : {'Name': ['Amar', 'Akbar', 'Motilal'], 'Salary': [3.0, 5.0, 19.0], 'Age': [23, 30, 50], 'Id': [1, 2, 4]}

"""

""" Create set of dictonary keys."""
sets = { "Id","Name","Age","Salary"}

"""Create dictonary using set value as a key and list as values."""
dct = {}
for i in sets:
	dct[i] = []

""" Get input from user and insert it into the dictonary.""" 
while True:
	(dct['Id']).append(int(input("Enter Id:"))) 
	(dct['Name']).append(input("Enter Name:").title()) 
	(dct['Age']).append(int(input("Enter Age:"))) 
	(dct['Salary']).append(float(input("Enter salary in LPA:")))
	if input("Do you want to add one more entery YES or NO:").lower() == "no":
		break
		
"""Print Final dictonary."""
print ("Your dictonary :",dct) 


""" Create a set of Id's."""
sets = set(dct['Id'])
lst = list(sets)
print (lst)

"""Remove duplicate Id's from dictonary."""
c = 0
for i in dct['Id']:
	if i in lst:
		lst.remove(i)
	else:
		(dct['Id']).pop(c)
		(dct['Name']).pop(c)
		(dct['Age']).pop(c)
		(dct['Salary']).pop(c)
	c = c+ 1

"""Print dictonary."""
print ("Dictnary after removing duplicate Id's :",dct) 
