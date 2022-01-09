import sys 
input = sys.stdin.readline

n = int(input())
plans = [0]
for i in range(n):
    T,P = map(int,input().split())
    plans.append((T,P))

dp = [0]*(n+1)
current = dp[n]
for i in range(n,0,-1):
    ti,pi = plans[i]
    if i-1+ti <= n: #기간 안에 상담이 가능한 경우 
        if i+ti<=n : 
            dp[i]= max(pi+dp[i+ti],current)
            current = dp[i]
        else: # 상담이 마지막날에 정확히 끝나는 경우 
            dp[i]= max(pi,current)
            current = dp[i]
    else: # 상담 불가능한 경우 
        dp[i] = current
        current = dp[i]
print(max(dp))