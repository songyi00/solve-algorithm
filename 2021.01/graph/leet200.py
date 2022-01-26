from collections import deque
visit = [[False for _ in range(5)]for _ in range(4)] 

def bfs(island,i,j):
    queue = deque()
    queue.append((i,j))
    while queue:
        x,y = queue.popleft()
        visit[x][y] = True 
        dx = [1,-1,0,0]
        dy = [0,0,1,-1]

        for k in range(4):
            kx = x +dx[k]
            ky = y +dy[k]
 
            if 0<=kx<4 and 0<=ky<5 : #행 열 
               if island[kx][ky]=='1' and not visit[kx][ky]:
                   queue.append((kx,ky))
                   island[kx][ky] = 0

def main():
    island = [list(input()) for _ in range(4)]
    count = 0
    for i in range(len(island)):
        for j in range(len(island[i])):
            if island[i][j] == '1':
                bfs(island,i,j)
                count += 1 
    print(count)

if __name__ == "__main__":
    main()

"""
11110
11010
11000 
00000
"""