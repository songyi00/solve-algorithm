import sys 
input = sys.stdin.readline 

stairs = [0] 
n = int(input())
for _ in range(n):
    stairs.append(int(input()))
dp = [0]*(n+1)

for i in range(1,n+1):
    if i <= 2 :
        dp[i] = dp[i-1] + stairs[i]
        continue
    dp[i] = max(dp[i-2]+stairs[i], dp[i-3]+stairs[i-1]+stairs[i])    
print(dp[n])