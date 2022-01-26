from collections import defaultdict
import heapq

INF = float('inf')

def dijkstra(edges,K):
    queue = []
    distance = defaultdict(lambda :INF)
    found = defaultdict(lambda : False)
    heapq.heappush(queue,(0,K))
    distance[K]= 0

    while queue:
        v = heapq.heappop(queue)
        found[v[1]] = True
        for nextV in edges[v[1]]:
            node = nextV[0]
            cost = nextV[1]
            if distance[v[1]]+cost < distance[node] and not found[node]:
                distance[node]= distance[v[1]] + cost
                heapq.heappush(queue,(distance[node],node))
    return distance

def main():
    V, E = map(int,input().split()) #정점 개수, 간선 개수 
    K = int(input()) #시작점 
    edges = defaultdict(list)
    
    for _ in range(E):
        u,v,w = map(int,input().split())
        edges[u].append((v,w))
    
    distance = dijkstra(edges,K)

    #print(distance)
    for i in range(1,V+1):
        if distance[i] == INF:
            print('INF')
        else:
            print(distance[i]) 

if __name__ == "__main__":
    main()