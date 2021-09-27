import sys
input = sys.stdin.readline 

n = int(input())
times = []
for _ in range(n):
    start,end = map(int,input().split())
    times.append((start,end))

times = sorted(times,key= lambda x : (x[1],x[0]))
current = times[0][1]
cnt = 0
for i,time in enumerate(times):
    if i == 0:
        cnt += 1
        continue
    if time[0] >= current: 
        cnt += 1 
        current = time[1]
print(cnt)