m,n = int(input()),int(input())

lst = [0]*(m-1)+[1]

for i in range(n-m):
	lst.append(sum(lst[i:i+m]))
print(lst)
