from collections import defaultdict, deque
n = int(input())
computers = [list(map(int,input().split())) for _ in range(n)]
nums = []
visit = defaultdict(lambda : False)
def bfs(node):
    queue = deque([node])
    while queue:
        node = queue.popleft()
        visit[node] = True
        for idx in range(n):
            if computers[node][idx] == 1 and not visit[idx]:
                queue.append(idx)
        
cnt = 0
for i in range(n):
    for j in range(n):
        if i == j:
            continue
        if computers[i][j] == 1 and not visit[i]:
            bfs(i)
            cnt +=1 
for i in range(n):
    if not visit[i]:
        cnt+=1
print(cnt)