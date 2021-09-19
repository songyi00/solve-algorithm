from collections import defaultdict
import heapq
import sys
input = sys.stdin.readline

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def dijkstra(graph):
    visit = defaultdict(lambda:False)
    distance = defaultdict(lambda: float('inf'))
    queue = []
    heapq.heappush(queue,(graph[0][0],0,0)) # 비용, 행, 열 
    distance[(0,0)] = 0

    while queue:
        cost,r,c = heapq.heappop(queue)
        visit[(r,c)] = True
        for i in range(4):
            nx = dx[i] + c
            ny = dy[i] + r 

            if 0<=nx<n and 0<=ny<n:
                if cost + graph[ny][nx] < distance[(ny,nx)] and not visit[(ny,nx)]:
                    distance[(ny,nx)] = cost + graph[ny][nx]
                    heapq.heappush(queue,(distance[(ny,nx)] , ny, nx))

    return distance[(n-1,n-1)]

cnt = 1
while True:
    n = int(input())
    if not n:
        break
    else:
        graph = [list(map(int,input().split())) for _ in range(n)]
        print("Problem {}: {}".format(cnt,dijkstra(graph)))
        cnt +=1