import sys 
input = sys.stdin.readline 

n = int(input())
schedule_list = [0]
dp = [0 for _ in range(n+1)]
for _ in range(n):
    a,b = map(int,input().split())
    schedule_list.append((a,b))
current = dp[n]
for i in range(n,0,-1):
    day,price = schedule_list[i]
    if i+day<= n: #상담 잡을 수 있는 경우 
        dp[i] = max(dp[i+day]+price,current)
        current = dp[i]
    elif i+day-1 == n:#마지막 상담인 경우 
        dp[i] = max(price,current)
        current = dp[i]
    else: #상담 잡을 수 없는 경우 
        dp[i] = current
        current = dp[i]

print(dp[1])