from collections import deque

max_result = 0

def bfs(matrix): # 바이러스 퍼트리기 
    global max_result
    queue = deque()
    copy = [[0] * len(matrix[0]) for i in range(len(matrix))]

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            copy[i][j] = matrix[i][j]

    for i in range(len(copy)):
        for j in range(len(copy[0])):
            if copy[i][j] == 2: 
                queue.append((i,j))
    
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    while queue:
        x, y = queue.popleft()       
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<len(copy) and 0<=ny<len(copy[0]):
                if copy[nx][ny] == 0:
                    queue.append((nx,ny))
                    copy[nx][ny] = 2
    result = 0 
    for i in range(len(copy)):
        for j in range(len(copy[0])):
            if copy[i][j] == 0:
                result+=1
    max_result = max(max_result,result) 

def wall(n,m,matrix,count): # 벽세우기 
    if count == 3:
        bfs(matrix)
        return
    for i in range(n):
        for j in range(m):
            if matrix[i][j]==0:
                matrix[i][j] = 1
                wall(n,m,matrix,count+1)
                matrix[i][j] = 0


def main():
    n, m = map(int,input().split())
    matrix = [list(map(int,input().split())) for _ in range(n)]
    wall(n,m,matrix,0)
    print(max_result)
    
if __name__ == "__main__":
    main()