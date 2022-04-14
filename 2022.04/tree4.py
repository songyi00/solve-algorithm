import sys
input = sys.stdin.readline 

n = int(input())
matrix = []
for _ in range(n):
    matrix.append(list(map(int,input().split())))

dx = [0,1]
dy = [1,0]

result = []
route = []

def dfs(i,j):
    global route
    if i == n-1 and j == n-1:
        result.append(route.copy())
        return
    for k in range(2):
        ny = dy[k] + i
        nx = dx[k]+ j
        if 0<=ny<n and 0<=nx<n:
            route.append(matrix[ny][nx])
            dfs(ny,nx)
            route.pop()
            
route = [matrix[0][0]]

dfs(0,0)

# print(result)   
final_result = []
for r in result:
    max_val = max(r)
    val = sum(r)+max_val
    final_result.append(val)
print(max(final_result))
    
