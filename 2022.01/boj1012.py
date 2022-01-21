from collections import deque,defaultdict

t = int(input())

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(y,x):
    queue = deque([(y,x)])

    while queue:
        i,j = queue.popleft()    
        matrix[i][j] = 0
        
        for k in range(4):
            nx = dx[k]+j
            ny = dy[k]+i
            if 0<=nx<m and 0<=ny<n and matrix[ny][nx]:
                matrix[ny][nx] = 0
                queue.append((ny,nx))
                
                
for _ in range(t):
    m,n,k = map(int,input().split())
    matrix = [[0]*m for _ in range(n)]
    cabbages = []
    for _ in range(k):
        x,y = map(int,input().split())
        matrix[y][x] = 1
        cabbages.append((y,x))
    
    cnt = 0
    for y,x in cabbages:
        if matrix[y][x]:
            bfs(y,x)
            cnt += 1
    print(cnt)