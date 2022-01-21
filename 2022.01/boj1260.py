import sys 
input = sys.stdin.readline
from collections import deque,defaultdict

def dfs(graph,v,n):
    print(v,end=' ')
    visit[v] = 1
    for i in range(1,n+1):
        if i in graph[v] and not visit[i]:
            dfs(graph,i,n) 
            
def bfs(graph,v,n):
    queue = deque([v])
    while queue:
        node = queue.popleft()
        visit[node] = 0
        print(node,end=' ')
        for i in range(1,n+1):
            if i in graph[node]and visit[i] == 1:
                if i not in queue:
                    queue.append(i)
                
#def dfs(graph,v,n):
    
n,m,v = map(int,input().split())
graph = defaultdict(list)
visit = [0]*(1+n)

for i in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)    
    graph[b].append(a)

dfs(graph,v,n)
print()
bfs(graph,v,n)