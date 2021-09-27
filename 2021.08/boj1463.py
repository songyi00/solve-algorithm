
n = int(input())

dp = [0]*(n+1)

for i in range(1,n+1):
    if i == 1 :
        dp[i] = 0
    elif i == 2 :
        dp[i] = 1
    elif i == 3:
        dp[i] = 1
    else:
        result = [dp[i-1]+1] 
        if i%2 == 0:
            result.append(dp[i//2]+1)
        if i%3 == 0:
            result.append(dp[i//3]+1)
        dp[i] = min(result)

print(dp[n])