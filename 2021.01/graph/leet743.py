from collections import defaultdict
import heapq
def daijkstra(k,graph):
    queue = []
    found = defaultdict(lambda : False) 
    distance = defaultdict(lambda : float('inf'))
    heapq.heappush(queue,(0,k)) # 비용, 정점 
    distance[k]=0
    while queue:
        v = heapq.heappop(queue)
        found[v[1]] = True
        for nextV in graph[v[1]]:
            node = nextV[0]
            cost = nextV[1]
            if distance[v[1]]+cost < distance[node] and not found[node]:
                distance[node]= distance[v[1]] + cost
                heapq.heappush(queue,(cost,node))
    return distance

def main():
    n, k = input().split() #전체 노드 개수, 출발점 
    graph = defaultdict(list)
    while True:
        try:
            a,b,c = input().split() #출발지, 도착지, 비용 
            graph[a].append((b,int(c))) 
        except:
            distance = daijkstra(k,graph)
            print()
            if len(distance) == int(n) :
                print(max(distance.values()))
            else :
                print(-1)
            exit()

if __name__ == "__main__":
    main()