def main():
    N = int(input())
    dp = [0 for _ in range(N)]
    for i in range(len(dp)):
        if i == 0:
            dp[i]=1
        elif i==1:
            dp[i]=1
        else:
            dp[i] = dp[i-1]+dp[i-2]
            
    print(dp[N-1])

if __name__ == '__main__':
    main()