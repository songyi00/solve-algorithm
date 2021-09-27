from collections import defaultdict, deque
import sys 
input = sys.stdin.readline

def bfs(start=1):
    queue = deque()
    visit = defaultdict(lambda : False)
    queue.append(start)
    cnt = 0
    while queue:
        node = queue.popleft()
        cnt += 1
        visit[node] = True
        for nextV in graph[node]:
            if not visit[nextV] and nextV not in queue:
                queue.append(nextV)

    return cnt-1

v = int(input())
e = int(input())
graph = defaultdict(list)

for _ in range(e):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

print(bfs())