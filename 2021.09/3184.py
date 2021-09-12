from collections import defaultdict,deque
import sys
input = sys.stdin.readline 

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(i,j):
    queue = deque()
    visit = defaultdict(lambda:False)
    queue.append((i,j))
    o,v = 0,0
    while queue:
        i,j = queue.popleft()
        if matrix[i][j] == 'v':
            v+=1
        elif matrix[i][j] =='o':
            o+=1
        matrix[i][j] = '#'
        
        for k in range(4):
            ny = i+ dy[k]
            nx = j+ dx[k]
            if 0<=ny<r and 0<=nx<c:
                if matrix[ny][nx] !='#' and not visit[(ny,nx)]:
                    queue.append((ny,nx))
                    visit[(ny,nx)] = True # 바로 표시해도 됨 
                
    return o,v

r,c = map(int,input().split())
matrix = [list(input().strip()) for _ in range(r)]

result1, result2 = 0, 0 # 양, 늑대
for i in range(r):
    for j in range(c):
        if matrix[i][j] != '#':
            o,v = bfs(i,j)
            if v>=o:
                result2 +=v
            else:
                result1 +=o

print(result1,result2)
