from collections import deque
import sys

input = sys.stdin.readline

def bfs(start):
    queue = deque()
    visit = [0] * (n+1)
    queue.append(start)
    visit[start] = 1 
    cnt = 0
    while queue:
        v = queue.popleft()
        cnt+=1 
        for nextV in graph[v]:
            if not visit[nextV]:
                queue.append(nextV)
                visit[nextV] = 1
    return cnt 

n,m = map(int,input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a,b = map(int,input().split())
    graph[b].append(a)

result = []
compare = 0
for i in range(1,n+1):
    if graph[i]:
        temp = bfs(i)
        if compare <=temp:
            if compare < temp :
                result = []
            result.append(i)
            compare = temp 
print(*result)

