from collections import defaultdict
import heapq

import sys 
input = sys.stdin.readline 

def dijkstra(start):
    distance= defaultdict(lambda:float('inf'))
    found = defaultdict(lambda:False)
    queue = []
    heapq.heappush(queue,(0,start))
    distance[start] = 0

    while queue:
        cost, node = heapq.heappop(queue)
        found[node] = True
        for next_cost, next_node in edges[node]:
            if cost+next_cost < distance[next_node] and not found[next_node]:
                distance[next_node] = cost+next_cost
                heapq.heappush(queue,(distance[next_node],next_node))

    return distance


N,E= map(int,input().split())
edges = defaultdict(list)
for _ in range(E):
    a,b,c = map(int,input().split())
    edges[a].append((c,b))
    edges[b].append((c,a))

target1, target2 = map(int,input().split())

route1 = dijkstra(1)[target1]+dijkstra(target1)[target2]+dijkstra(target2)[N]
route2 = dijkstra(1)[target2]+dijkstra(target2)[target1]+dijkstra(target1)[N]

result = min(route1,route2)
if result < float('inf'):
    print(result)
else:
    print(-1)