def main(): 
    n = int(input())
    dp = [0 for _ in range(n+1)]

    for i in range(1,n+1):
        if i <= 2:
            dp[i] = i
            continue
        dp[i] = dp[i-1] + dp[i-2]
    print(dp[n])

if __name__ == "__main__":
    main()

"""
계단 오르기 
매번 각각 1계단 또는 2계단만 가능 
"""