import itertools 

import sys 
input = sys.stdin.readline 

n = int(input())
f = list(map(int,input().split()))

pool = itertools.combinations(f,2)
current = -float('inf')
for a,b in pool:
    current = max(current, a*b)

print(current)