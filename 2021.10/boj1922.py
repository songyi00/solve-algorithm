from collections import defaultdict
import sys
input = sys.stdin.readline

def find_parent(x):
    if parent[x] == x: # 부모 존재하지 않는 경우
        return parent[x]
    else: # 존재하는 경우 
        parent[x]= find_parent(parent[x]) # 가장 상위 부모를 찾음 
        return parent[x]
    
def merge(a,b):
    a_ = find_parent(a)
    b_ = find_parent(b)
    if a_ != b_ :
        parent[a_]=b_
        return True
    return False         
    
N = int(input())
M = int(input())

parent = defaultdict(int)
for i in range(1,N+1):
    parent[i]= i
    
edges = []
for _ in range(M):
    edges.append(list(map(int,input().split())))

edges.sort(key=lambda x: x[2])
cost = 0
for e in edges:
    a,b,c = e[0],e[1],e[2]
    if merge(a,b):
        cost+=c
#print(edges)
print(cost)