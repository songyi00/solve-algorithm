from collections import defaultdict
import sys
input = sys.stdin.readline 

dx = [-1,1,0,0]
dy = [0,0,-1,1]

visit = defaultdict(lambda : False)
result = 0

def dfs(i,j,cnt):
    global result 
    
    if result == 26:
        return
    
    result = max(result,cnt)
    
    for k in range(4):
        nx = dx[k]+j
        ny = dy[k]+i
        
        if 0<=nx<c and 0<=ny<r:
            if not visit[matrix[ny][nx]]:
                visit[matrix[ny][nx]] = True
                dfs(ny,nx,cnt+1)
                visit[matrix[ny][nx]] = False

r,c = map(int,input().split())
matrix = []

for i in range(r):
    matrix.append(list(input()))

visit[matrix[0][0]]= True
dfs(0,0,1)
print(result)

