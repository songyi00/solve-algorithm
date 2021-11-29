import sys
input = sys.stdin.readline 
from collections import deque

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(i,j):
    queue = deque()
    queue.append((i,j))
    while queue:
        row,col = queue.popleft()
        matrix[row][col] = 0

        for l in range(4):
            nx = dx[l]+col
            ny = dy[l]+row
            if 0<=nx<m and 0<=ny<n and (ny,nx) not in queue:
                if matrix[ny][nx]==1:
                    queue.append((ny,nx))

t = int(input())
for _ in range(t):
    m,n,k = map(int,input().split()) # 가로,세로,배추개수
    matrix = [[0]*m for _ in range(n)]
    location = []
    for _ in range(k):
        x,y = map(int,input().split())
        matrix[y][x] = 1 
        location.append((x,y))
    cnt = 0
    for locate in location:
        x, y = locate 
        if matrix[y][x]==1:
            bfs(y,x)
            cnt+=1 
    print(cnt)