from collections import defaultdict
import sys 
input = sys.stdin.readline

count = 0 
visit = defaultdict(lambda : False)
def dfs(node):
    global count,visit
    visit[node] = True 
    for num in graph[node]:
        if not visit[num]:
            count+=1
            dfs(num)
        
n = int(input())
m = int(input())
graph = defaultdict(list)
for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
dfs(1)
print(count)