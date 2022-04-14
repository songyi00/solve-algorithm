import itertools


def dfs(n,m,depth):
    if depth == m :
        print(*array)
        return 
    
    for i in range(1,n+1):
        if not visit[i]:
            visit[i] = 1
            array.append(i)
            dfs(n,m,depth+1)
            visit[i] = 0
            array.pop()
n, m = map(int,input().split())
array = []
visit = [0 for _ in range(n+1)]

dfs(n,m,0)

print("========================")
test = [i for i in range(1,n+1)]
for j in itertools.combinations(test,2):
    print(j)