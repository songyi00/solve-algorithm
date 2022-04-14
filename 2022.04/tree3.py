import sys
input = sys.stdin.readline 

n,m = map(int,input().split())
matrix = []
for _ in range(n):
    matrix.append(list(map(int,input().split())))
    
l1,r1 = map(int,input().split())
l2,r2 = map(int,input().split())

for i in range(n):
    for j in range(m):
        if l1-1<=i<=r1-1:
            if matrix[i][j] == 1:
                matrix[i][j] = 0
                break

for i in range(n):
    for j in range(m):
        if l2-1<=i<=r2-1:
            if matrix[i][j] == 1:
                matrix[i][j] = 0
                break

cnt = 0
for i in range(n):
    for j in range(m):
        if matrix[i][j] == 1:
            cnt +=1
print(cnt)