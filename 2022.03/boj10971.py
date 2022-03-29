import itertools
import sys 
input = sys.stdin.readline 

N = int(input()) # 도시의 수 
cost_matrix = []
for _ in range(N):
    cost_matrix.append(list(map(int,input().split())))

pool = [i for i in range(0,N)]

def find_distance(route):
    sum = 0
    for i in range(N-1):
        val = cost_matrix[route[i]][route[i+1]]
        if val == 0:
            return -1 
        sum += val 
    val = cost_matrix[route[i+1]][route[0]]
    if val == 0:
            return -1 
    sum += val
    return sum 

current = float('inf')
for i in itertools.permutations(pool):
    dist = find_distance(i) 
    if dist != -1:
        current = min(current,dist)

print(current)