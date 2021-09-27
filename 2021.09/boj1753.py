from collections import defaultdict
import heapq
import sys

input = sys.stdin.readline 

def dijkstra(start,edges):
    distance = defaultdict(lambda:float('inf'))
    distance[start]=0
    queue = []
    heapq.heappush(queue,(0,start)) #비용, 정점
    found = defaultdict(lambda : False)

    while queue:
        weight , node = heapq.heappop(queue)
        found[node] = True

        for nextNode in edges[node]:
            if weight+ nextNode[0] < distance[nextNode[1]] and not found[nextNode[1]]:
                distance[nextNode[1]] = weight + nextNode[0]
                heapq.heappush(queue,(distance[nextNode[1]],nextNode[1]))

    return distance

V,E = map(int,input().split())
start = int(input())

edges = defaultdict(list)

for _ in range(E):
    u,v,w = map(int,input().split())
    edges[u].append((w,v))

distance = dijkstra(start,edges)
for i in range(1,V+1):
    if distance[i] == float('inf'):
        print('INF')
    else:
        print(distance[i])
