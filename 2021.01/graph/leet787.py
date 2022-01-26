from collections import defaultdict
import heapq

def daijkstra(edges,k,src,dst):
    queue = []
    heapq.heappush(queue,(0,src,k)) #비용,정점,경유지 개수
    found = defaultdict(lambda: False)
    distance = defaultdict(lambda : float('inf'))
    distance[src] = 0
    while queue:
        v = heapq.heappop(queue)
        found[v[1]] = True
        count = v[2]
        if count>=0:
            for nextV in edges[v[1]]:
                node = nextV[0]
                cost = nextV[1]
            
                if distance[v[1]] + cost < distance[node] and not found[node] :
                    distance[node] = distance[v[1]]+ cost
                    heapq.heappush(queue,(cost,node,count-1))

    return distance

def main():
    n,k = map(int,input().split()) #n개의 노드개수, k개의 경유지 
    src,dst = input().split()
    edges = defaultdict(list)
    while True:
        try:
            a,b,c = input().split()
            edges[a].append((b,int(c)))
        except :
            distance = daijkstra(edges,k,src,dst)
            if len(distance)== n:
                print(distance[dst])
            else:
                print(-1)
            exit()

            
if __name__ == "__main__":
    main()

"""
k개의 경유지 내에 최단 경로 
"""