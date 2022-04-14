T = int(input())

dp = [1,1,1,2,2]

inputs = []
for _ in range(T):
    inputs.append(int(input()))

max_n = max(inputs)
for i in range(5,max_n):
    dp.append(dp[i-1]+dp[i-5])

for i in inputs:
    print(dp[i-1])

    
    