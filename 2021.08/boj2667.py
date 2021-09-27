from collections import defaultdict,deque
import sys 

input = sys.stdin.readline

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(i,j):
    queue = deque()
    queue.append((i,j))
    count = 0
    while queue:
        r,c = queue.popleft()
        visit[r][c] = True
        apartment[r][c] = 0 
        count+=1

        for i in range(4):
            nx = c + dx[i]
            ny = r + dy[i]

            if 0<=nx<n and 0<=ny<n and not visit[ny][nx]:
                if apartment[ny][nx] == 1 and (ny,nx) not in queue:
                    queue.append((ny,nx))

    return count 

n = int(input())
apartment = [list(map(int,input().strip())) for _ in range(n)]
visit = [[False]*n for _ in range(n)]
cnt = 0
num_list = [] 

for i in range(n):
    for j in range(n):
        if apartment[i][j] == 1:
            num_list.append(bfs(i,j))
            cnt += 1 

print(cnt)
num_list.sort()
for num in num_list:
    print(num)
