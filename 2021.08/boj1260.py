"""
1~N 정점에 대해 시작점 v에서 dfs, bfs 탐색
정점이 여러개인 경우 작은 정점부터 탐색해야하므로 2차원 배열 만들어서 구현 
"""
import sys
from collections import deque

input = sys.stdin.readline

def dfs(v,graph):
    print(v, end=' ')
    visit[v] = 1 # 방문한 점 1로 
    for i in range(1,n+1):
        if visit[i] == 0 and graph[v][i] == 1:
            dfs(i,graph)

def bfs(v,graph):
    queue = deque()
    queue.append(v)

    while queue:
        v = queue.popleft()
        print(v,end=' ')
        visit[v] = 0 # 방문한 점 0으로 
        for i in range(1,len(graph[v])):
            if graph[v][i] == 1 and visit[i] == 1:
                if i not in queue:
                    queue.append(i)

n,m,v = map(int,input().split())
graph = [[0]*(n+1) for _ in range(n+1)]
visit = [0]*(n+1)
for _ in range(m):
    a,b = map(int,input().split())
    graph[a][b] = 1
    graph[b][a] = 1

#print(graph)
dfs(v,graph)
print()
bfs(v,graph)
