current = float('inf')
def dfs(matrix,cost,x,y,n):
    global current
    dy = [-2,-1,1,2] #양 옆으로 갈 수 있는 위치 
    
    for i in range(4):
        nx = x+1
        ny = y+dy[i]
        if nx == n : #비용 탐색이 끝난 경우 
            current = min(current,cost)
            print(cost)
            break
        elif 0<=nx<n and 0<=ny<3:
            cost += matrix[nx][ny]
            dfs(matrix,cost,nx,ny,n)
            cost -= matrix[nx][ny]

def main():
    n = int(input())
    matrix = []
    for i in range(n):
        matrix.append(list(map(int,input().split())))
    for i in range(3):
        dfs(matrix,matrix[0][i],0,i,n)
    print(current)

if __name__ == '__main__':
    main()
 
# dfs + 백트래킹으로 풀었더니 답은 맞는 것 같지만 시간초과가 나는 풀이이다. 