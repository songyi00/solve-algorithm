from collections import deque
def dfs(a,b,n,matrix,count):
    matrix[a][b]= '0'
    dx = [1,-1,0,0]
    dy = [0,0,-1,1]

    for i in range(4):
        x = a+dx[i]
        y = b+dy[i]
        if 0<=x<n and 0<=y<n:
            if matrix[x][y]=='1':
                count = dfs(x,y,n,matrix,count+1)
    return count 


def main():
    n = int(input())
    matrix = [list(input()) for _ in range(n)]
    result = []
    for i in range(n):
        for j in range(n):
            if matrix[i][j] == '1':
                result.append(dfs(i,j,n,matrix,1))
    print(len(result))
    result.sort()
    for r in result:
        print(r)
        
if __name__ == "__main__":
    main()