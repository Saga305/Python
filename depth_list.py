"""
Test case:
Enter a number:1
Depth of 1 in given list [1, 2, 3, [4, 5, 6, [7, 8, 9], 14], 10] is [0]

Test case:
Enter a number:2
Depth of 2 in given list [1, 2, 3, [4, 5, 6, [7, 8, 9], 14], 10] is [1]

Test case:
Enter a number:3
Depth of 3 in given list [1, 2, 3, [4, 5, 6, [7, 8, 9], 14], 10] is [2]

Test case:
Enter a number:4
Depth of 4 in given list [1, 2, 3, [4, 5, 6, [7, 8, 9], 14], 10] is [3][0]

Test case:
Enter a number:5
Depth of 5 in given list [1, 2, 3, [4, 5, 6, [7, 8, 9], 14], 10] is [3][1]

Test case:
Enter a number:6
Depth of 6 in given list [1, 2, 3, [4, 5, 6, [7, 8, 9], 14], 10] is [3][2]

Test case:
Enter a number:7
Depth of 7 in given list [1, 2, 3, [4, 5, 6, [7, 8, 9], 14], 10] is [3][3][0]

Test case:
Enter a number:8
Depth of 8 in given list [1, 2, 3, [4, 5, 6, [7, 8, 9], 14], 10] is [3][3][1]

Test case:
Enter a number:14
Depth of 14 in given list [1, 2, 3, [4, 5, 6, [7, 8, 9], 14], 10] is [3][4]

Test case:
Enter a number:10
Depth of 10 in given list [1, 2, 3, [4, 5, 6, [7, 8, 9], 14], 10] is [4]

Test case:
Enter a number:11
Element 11 is not present in given list [1, 2, 3, [4, 5, 6, [7, 8, 9], 14], 10].
"""

def depth(lst):
    global st
    total = 0
    for element in lst:
        if (type(element) == type([])):
            total = total + 1
            if depth(element) == True:
               st = "[" + str(total-1) +"]" + st
               return True
        else:
            if element == n:
               st += "[" + str(total) + "]"
               return True
            total = total + 1

st=""
n = int(input("Enter a number:"))
lst = [1,2,3,[4,5,6,[7,8,9],14],10]
depth(lst)
if st == "":
	print("Element {} is not present in given list {}.".format(n,lst))
else:
	print("Depth of {} in given list {} is {}".format(n,lst,st))
