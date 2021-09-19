import heapq
import sys

input = sys.stdin.readline 
array = []
n = int(input())
for _ in range(n):
    num = int(input())
    if num:
        heapq.heappush(array,-num)
    else:
        if array:
            print(-heapq.heappop(array))
        else: 
            print(0)
