import sys
from collections import deque
input = sys.stdin.readline 

nx = [-1,1,0,0]
ny = [0,0,-1,1]

def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    k = 0
    while queue:
        x,y = queue.popleft()
        apartment[y][x] = 0 
        k += 1 # 단지 내 집의 수 세기 

        for i in range(4):
            dx = nx[i] + x  #열 
            dy = ny[i] + y  #행 
            
            if 0<=dx<n and 0<=dy<n and apartment[dy][dx]:
                if (dx,dy) not in queue:
                    queue.append((dx,dy))
    return k 

n = int(input())
apartment = [list(map(int,input().strip())) for _ in range(n)]
cnt = 0 
num_list = [] 
for i in range(n):
    for j in range(n):
        if apartment[i][j] == 1:
            num = bfs(j,i)
            num_list.append(num)
            cnt += 1
 
num_list.sort()
print(cnt)
for num in num_list:
    print(num)