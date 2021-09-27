from collections import defaultdict, deque
import sys 

input = sys.stdin.readline

def bfs(x0,y0):
    queue = deque()
    queue.append((x0,y0,20))
    visit = defaultdict(lambda : False)

    while queue :
        x0,y0,num = queue.popleft()
        visit[(x0,y0)] = True
        if x0 == x1 and y0 == y1 :
                print('happy')
                return
        for node in nodes:
            nx,ny = node
            d = abs(nx-x0) + abs(ny-y0)
            if num*50 >= d and not visit[(nx,ny)]:
                queue.append((nx,ny,20))
    print('sad')
    return 

t = int(input())
for _ in range(t): # 테스트케이스 개수만큼 돌리기 
    n = int(input())
    x0,y0 = map(int,input().split())
    nodes = []
    for _ in range(n): # 편의점 개수만큼 돌리기 
        x,y = map(int,input().split())
        nodes.append((x,y))
    x1,y1 = map(int,input().split())
    nodes.append((x1,y1))
    bfs(x0,y0)
        