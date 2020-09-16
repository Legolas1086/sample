import numpy as np

n,m=input().split()
n,m=int(n),int(m)
matrix=[]
for i in range(n):
    matrix.append(input().split())
print(matrix) 
matrix=np.array(matrix).reshape(n,m)
print(matrix[1][1])
s=0
d=0

for i in range(n):
    s=s+int(matrix[i][0])
print(s)    