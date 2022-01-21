import sys
from collections import defaultdict
import heapq
input = sys.stdin.readline 

"""
1번 정점에서 N 번 정점으로 이동 
간선 v1,v2 를 반드시 거치는 최단 경로 
"""
    
def dijkstra(start):
    distance = defaultdict(lambda : float('inf'))
    found =defaultdict(lambda : False)
    queue = []
    heapq.heappush(queue,(0,start)) # (비용,정점) 
    distance[start] = 0
    while queue:
        weight,node = heapq.heappop(queue)
        found[node] = True
        for next_n in edges[node]:
            next_c, next_node = next_n
            if weight + next_c < distance[next_node] and not found[next_node]:
                distance[next_node] = weight + next_c 
                heapq.heappush(queue,(distance[next_node],next_node))
    return distance

N,E = map(int,input().split())
edges = defaultdict(list)

for i in range(E):
    a,b,c = map(int,input().split())
    edges[a].append((c,b))
    edges[b].append((c,a))
    
tar1,tar2 = map(int,input().split())

start = dijkstra(1)
mid1 = dijkstra(tar1)
mid2 = dijkstra(tar2)

result = min(start[tar1] + mid1[tar2] + mid2[N], start[tar2] + mid2[tar1] + mid1[N])

if result < float('inf'):
    print(result)
else:
    print(-1)