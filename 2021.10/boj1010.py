n = int(input())

matrix = []
for _ in range(n):
    matrix.append(list(map(int,input().split())))

dp =  [matrix[0]]+ [[0]*3 for _ in range(n-1)]

#print(dp)
for i in range(1,n):
    dp[i][0] = min(dp[i-1][1]+matrix[i][0], dp[i-1][2]+matrix[i][0])
    dp[i][1] = min(dp[i-1][0]+matrix[i][1], dp[i-1][2]+matrix[i][1])
    dp[i][2] = min(dp[i-1][1]+matrix[i][2], dp[i-1][0]+matrix[i][2])

print(min(dp[n-1]))