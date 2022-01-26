import sys
sys.setrecursionlimit(10**6)

answer = 1 
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def dfs(count,x,y):
    global answer
    global route 
    answer = max(answer,count)
    # 상 하 좌 우 
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0<=nx<row and 0<=ny<col and board[nx][ny] not in route:
            route.append(board[nx][ny])
            dfs(count+1,nx,ny)
            route.pop()
        

row,col = map(int,input().split())
board = [list(input())for _ in range(row)]
route = [board[0][0]] 
dfs(1,0,0)
print(answer)


#DFS+백트래킹 
#말이 지날 수 있는 최대의 칸 수를 출력한다. 