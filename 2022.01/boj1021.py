import sys
from collections import deque
input = sys.stdin.readline

n,m = map(int,input().split())
queue = deque([i for i in range(1,n+1)])

idx = list(map(int,input().split()))
l_cnt, r_cnt = 0,0

for i in idx:
    if queue.index(i) <= len(queue)//2:
        for j in range(queue.index(i)):
            queue.append(queue.popleft())
            l_cnt+=1
        
    else: 
        for j in range(len(queue)-queue.index(i)): 
            queue.appendleft(queue.pop())
            r_cnt+=1
        
    queue.popleft()
    
print(l_cnt+r_cnt)