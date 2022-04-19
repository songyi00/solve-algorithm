
def dfs(n,m,depth,index):
    if depth == m:
        print(*array)
        return
    for i in range(index, n+1):
        array.append(i)
        dfs(n,m,depth+1,i)
        array.pop()
        
n, m = map(int,input().split())
array = []
dfs(n,m,0,1)