import sys 
input = sys.stdin.readline

def union_find(a):
    if parent[a] == a:
        return a 
    else:
        parent[a] = union_find(parent[a])
        return parent[a]

def merge(a,b):
    x = union_find(a)
    y = union_find(b)

    if x != y : # merge 할 수 있는 경우 
        parent[x] = y
        return True

n, m = map(int,input().split()) #건물개수, 도로개수 
edges = []
parent = [i for i in range(n+1)]
for _ in range(m+1):
    a,b,c = map(int,input().split())
    parent[a]=a
    parent[b]=b
    edges.append((a,b,int(c)))
edges.sort(key=lambda x:x[2])

fatigue = 0 
total_worst = 0

for u,v,w in edges:
    if merge(u, v):
        if w == 0:
            fatigue+=1
total_worst = fatigue**2

fatigue = 0 
total_best = 0 
edges.sort(key=lambda x:x[2],reverse=True)
parent = [i for i in range(n+1)]
for u,v,w in edges:
    if merge(u, v):
        if w == 0:
            fatigue+=1
total_best = fatigue**2
print(total_worst-total_best)
    
