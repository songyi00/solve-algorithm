from collections import defaultdict,deque
import sys
input = sys.stdin.readline 

visit = defaultdict(lambda:False)
cnt = 0
def dfs(node):
    global visit,cnt
    visit[node] = True
    cnt+=1
    for next_node in graph[node]:
        if not visit[next_node]:
            dfs(next_node)
    
def bfs(start):
    queue = deque([start])
    cnt = 0
    while queue:
        node = queue.popleft()
        visit[node] = True
        cnt+=1
        for next_node in graph[node]:
            if not visit[next_node] and next_node not in queue:
                queue.append(next_node)
    print(cnt-1)
    
n = int(input())
m = int(input())

graph = defaultdict(list)
for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

dfs(1)
print(cnt-1)