import sys
sys.setrecursionlimit(10**6)

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def dfs(matrix, height,x,y,visit):
    visit[x][y]= True

    for i in range(4):
        nx = x+ dx[i]
        ny = y+ dy[i]
        if 0<=nx<len(matrix) and 0<=ny<len(matrix[0]):
            if matrix[nx][ny]-height>0 and not visit[nx][ny]:
                dfs(matrix,height,nx,ny,visit)

def main():
    n = int(input())
    matrix = [list(map(int,input().split())) for _ in range(n)]
    
    max_result = []
    for m in matrix:
        max_result.append(max(m))
    MAX  = max(max_result)
    result = [1]
    for height in range(MAX+1):
        count = 0 
        visit = [[False for _ in range(n)] for _ in range(n)]
        
        for i in range(n):
            for j in range(n):
                if matrix[i][j]-height>0 and not visit[i][j]: # 안잠긴 부분을 세야 함 
                    dfs(matrix,height,i,j,visit)
                    count+=1 
        
        result.append(count)

    print(max(result))


if __name__ == "__main__":
    main()