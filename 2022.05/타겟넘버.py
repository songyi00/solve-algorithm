from collections import deque, defaultdict

cnt = 0
def dfs(n, depth, temp, numbers):
    global cnt 
    if n == depth :
        if temp == target:
            cnt += 1 
        return
    
    dfs(n+1, depth, temp+numbers[n], numbers)
    dfs(n+1, depth, temp-numbers[n], numbers)

def bfs(numbers):
    queue = deque()
    queue.append((0,0))
    depth = len(numbers)
    idx,cnt = 0,0
    while queue:
        val, idx = queue.popleft()
        if idx == depth:
            if val == target:
                cnt += 1
        elif idx < depth:
            queue.append((val-numbers[idx],idx+1))
            queue.append((val+numbers[idx],idx+1))
    return cnt
              
numbers = list(map(int,input().split()))
target = int(input())
#dfs(0,len(numbers),0,numbers)
print(bfs(numbers))