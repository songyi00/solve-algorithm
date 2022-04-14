def dfs(n,m,depth):
    if depth == m:
        print(*array)
        return
    
    for i in range(1,n+1):
        array.append(i)
        dfs(n,m,depth+1)
        array.pop()
        
n, m = map(int,input().split())
array = []

dfs(n,m,0)