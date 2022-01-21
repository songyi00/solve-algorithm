import sys
from collections import deque
input = sys.stdin.readline 

n = int(input())

stack = []
cnt = 1
result = []
flag = True

for i in range(n):
    num = int(input())
    while cnt<=num:
        stack.append(cnt)
        result.append("+")
        cnt +=1 
    
    if stack[-1] == num:
        stack.pop()
        result.append("-")
    else:
        flag = False
        break
if flag:
    for r in result:
        print(r)
else:
    print("NO")
    
# 1 2 3 4 5 6 7 8
# 4 3 6 8 7 5 2 1