from collections import deque,defaultdict

def bfs(n,k):
    queue = deque()
    count = 0
    queue.append((n,count))
    visit = defaultdict(lambda : False)
    while queue:
        v,count = queue.popleft()
        if not visit[v]:
            visit[v] = True
            if v == k:
                break
            else:
                count += 1 
                if (v-1) >=0:
                    queue.append((v-1,count))
                if (v+1) <= 100000:
                    queue.append((v+1,count))
                if (v*2) <= 100000:
                    queue.append((v*2,count))
    return count
        

def main():
    n, k = map(int,input().split())
    graph=defaultdict(list) 
    print(bfs(n,k))

if __name__ == "__main__":
    main()

