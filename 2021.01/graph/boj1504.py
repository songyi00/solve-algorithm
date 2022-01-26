from collections import defaultdict
import heapq
def dijkstra(edges,src,dst):
    queue = []
    heapq.heappush(queue,(0,src))
    distance = defaultdict(lambda : float('inf'))
    distance[src]= 0
    found = defaultdict(lambda : False)

    while queue:
        weight, v = heapq.heappop(queue)
        found[v] = True
        for nextV in edges[v]: #다음정점, 비용 
            if weight+nextV[1] < distance[nextV[0]] and not found[nextV[0]]:
                distance[nextV[0]] = weight + nextV[1]
                heapq.heappush(queue,(distance[nextV[0]],nextV[0]))
    return distance

def main():
    N,E = map(int,input().split())
    edges = defaultdict(list)
    for _ in range(E):
        a,b,c = map(int,input().split())
        edges[a].append((b,c))
        edges[b].append((a,c))
    v1,v2 = map(int,input().split())

    start = dijkstra(edges,1,N)
    mid1 = dijkstra(edges,v1,N)
    mid2 = dijkstra(edges,v2,N)
    
    result = min(start[v1] + mid1[v2] + mid2[N] , start[v2]+ mid2[v1] + mid1[N])

    if result<float('inf'):
        print(result)
    else:
        print(-1)

if __name__ == "__main__":
    main()