n = int(input())
size_list = list(map(int,input().split()))

dp = [1]*n #현재까지 넣을 수 있는 최대 상자 개수 

for i in range(1,len(dp)):
    for j in range(i+1):
        if size_list[j] < size_list[i]:
            dp[i] = max(dp[i],dp[j]+1)

print(max(dp))