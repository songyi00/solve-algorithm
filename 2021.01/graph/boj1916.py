from collections import defaultdict
import heapq
def dijkstra(edges,src,dst):
    queue = []
    heapq.heappush(queue,(0,src)) 
    distance = defaultdict(lambda : float('inf'))
    distance[src] = 0 
    found = defaultdict(lambda : False)

    while queue:
        weight, node = heapq.heappop(queue)
        found[node] = True
        for v in edges[node]: #v[0],v[1]: 정점, 정점까지 가는데 드는 비용 
            if v[1] + weight < distance[v[0]] and not found[v[0]]:
                distance[v[0]] = v[1] + weight
                heapq.heappush(queue,(distance[v[0]],v[0]))

    return distance[dst]

def main():
    N = int(input()) # 도시 개수(정점 개수)
    M = int(input()) # 버스 개수(간선 개수)
    edges = defaultdict(list)
    for _ in range(M):
        u,v,c = map(int,input().split())
        edges[u].append((v,c))
    src , dst = map(int,input().split())
    print(dijkstra(edges,src,dst))

if __name__ == "__main__":
    main()