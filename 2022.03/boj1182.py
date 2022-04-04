import itertools
import sys
input = sys.stdin.readline 

N ,S = map(int,input().split())
seq = list(map(int,input().split()))

cnt = 0
result = 0
for i in range(1,N+1):
    result = itertools.combinations(seq,i)
    #print(list(result))
    for j in result:
        if sum(j) == S :
            cnt +=1
    
print(cnt)