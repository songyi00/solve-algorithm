# 가장 긴 증가하는 부분 수열
n = int(input())
nums = list(map(int,input().split()))

dp = [1]*(n+1)

for i in range(len(nums)):
    for j in range(i+1):
        if nums[j] < nums[i] and dp[j]+1 > dp[i]:
            dp[i] = dp[j]+1

print(max(dp))