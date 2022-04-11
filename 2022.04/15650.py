from collections import defaultdict 

find = defaultdict(lambda : False)

def dfs(n,m,depth,index):
    if depth == m:
        print(*array)
        return
    
    for i in range(index,n+1):
        if not visit[i]:
            array.append(i)
            visit[i] = 1
            dfs(n,m,depth+1,i+1)
            array.pop()
            visit[i] = 0
            
n, m = map(int,input().split())
array = []
visit = [0 for _ in range(n+1)]
dfs(n,m,0,1)
