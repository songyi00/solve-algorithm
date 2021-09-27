import sys
input = sys.stdin.readline 

n = int(input())
T_i = [0]
P_i = [0]
for _ in range(n):
    t,p = map(int,input().split())
    T_i.append(t)
    P_i.append(p)

dp = [0]*(n+1)

for i in range(n,0,-1):
    if i+T_i[i]-1 <= n : # 날짜상 예약이 가능한 경우 
        if i == n: # 마지막 날인 경우 
            dp[i] = P_i[i]
        elif i+T_i[i] > n: # 이전에 잡힌 예약이 없는 경우 
            dp[i] = max(P_i[i],dp[i+1])
        else: 
            dp[i] = max(dp[i+T_i[i]]+P_i[i],dp[i+1])
    else: # 예약 불가능한 경우 
        if i != n:
            dp[i] = dp[i+1]

print(dp[1])