from collections import deque,defaultdict

def bfs(src,dst):
    queue = deque([(src,0)])
    visit = defaultdict(lambda: False)
    while queue :
        location,cnt = queue.popleft()
        if not visit[location]:
            visit[location] = True
            if location == dst:
                break
            else:
                if location-1 >=0:
                    queue.append((location-1,cnt+1))
                if location+1 <=100000:
                    queue.append((location+1,cnt+1))
                if location*2 <= 100000:
                    queue.append((location*2,cnt+1))
    return cnt 

n, k = map(int,input().split())
print(bfs(n,k))