import sys 

input = sys.stdin.readline

n, m = map(int,input().split())

A,B = [], []
def convert(i,j):
    for k in range(i,i+3):
        for l in range(j,j+3):
            if A[k][l]:
                A[k][l] = 0
            else:
                A[k][l] = 1
                 
for i in range(n):
    A.append(list(map(int,list(input().strip()))))
    
for i in range(n):
    B.append(list(map(int,list(input().strip()))))

cnt = 0
for i in range(n-2):
    for j in range(m-2):
        if A[i][j] != B[i][j]:
            convert(i,j)
            cnt+=1

result = True
for i in range(n):
    for j in range(m):
        if A[i][j] != B[i][j]:
            result = False
if result:
    print(cnt)    
else:
    print(-1)