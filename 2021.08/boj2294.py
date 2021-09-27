import sys 
input = sys.stdin.readline 

n,k = map(int,input().split())
coins = [int(input()) for _ in range(n)]
dp = [-1 for _ in range(k+1)]

for coin in coins:
    if len(dp) > coin :
        dp[coin] = 1 

for i in range(1,k+1):
    if dp[i] == 1:
        continue
    current = float('inf')
    for coin in coins:
        if i-coin > 0 and dp[i-coin] != -1 :
            current= min(current,dp[i-coin]+1)
            dp[i] = current

print(dp[k])