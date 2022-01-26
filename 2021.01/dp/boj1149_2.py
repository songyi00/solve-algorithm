def main():
    n = int(input())
    dp = []
    for _ in range(n):
        dp.append(list(map(int,input().split())))
    for i in range(1,n):
        dp[i][0] = min(dp[i-1][1],dp[i-1][2]) + dp[i][0] #Red 
        dp[i][1] = min(dp[i-1][0],dp[i-1][2]) + dp[i][1] #Green
        dp[i][2] = min(dp[i-1][0],dp[i-1][1]) + dp[i][2] #Blue 
    print(min(dp[n-1]))

if __name__ == '__main__':
    main()