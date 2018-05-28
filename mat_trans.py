#Matrix transpose using list.
m = [[1,2,3],[4,5,6],[7,8,9]]
for row in m :
    print(row)
res = []
for i in range(len(m[0])):
    new=[]
    for j in range(len(m)):
        new.append(m[j][i])
    res.append(new)

for row in res:
    print(row)

'''
Input:
[1, 2, 3]
[4, 5, 6]
[7, 8, 9]

Output:
[1, 4, 7]
[2, 5, 8]
[3, 6, 9]
'''
