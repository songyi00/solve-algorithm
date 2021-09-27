from collections import defaultdict,deque
import sys 
input = sys.stdin.readline 

def bfs(target1,target2):
    queue = deque()
    queue.append((target1,0))
    visit = defaultdict(lambda : False)
    while queue:
        node, num = queue.popleft()
        visit[node] = True

        if node == target2:
            return num

        for r in relation[node]:
            if not visit[r]:
                queue.append((r,num+1))
    return -1 

relation = defaultdict(list)
n = int(input())
target1, target2 = map(int,input().split())
m = int(input())

for _ in range(m):
    a,b = map(int,input().split())
    relation[a].append(b)
    relation[b].append(a)

print(bfs(target1,target2))
