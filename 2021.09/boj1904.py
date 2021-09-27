n = int(input())

dp = [0]*(n+1)

for i in range(1,n+1):
    if i <= 2:
        dp[i] = i
        continue

    dp[i] = (dp[i-2]+dp[i-1])%15746

print(dp[n])