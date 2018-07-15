import re
n = 7
m = 3
matrix = ['Tsi', 'h%x', 'i #', 'sM ', '$a ', '#t%', 'ir!']


mat = []
    
for i in range(m):
    for j in range(n):
        mat.append(matrix[j][i])
    
pattern = re.sub(r'(?<=\w)(\W+)(?=\w)',' ', "".join(mat))
print(pattern)