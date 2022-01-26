def main():
    N = int(input())
    dp = [0 for _ in range(41)]
    for i in range(0,41):
        if i == 0: 
            dp[i] = [1,0]
        elif i == 1:
            dp[i] = [0,1]
        else:
            dp[i] = [dp[i-1][0]+dp[i-2][0],dp[i-1][1]+dp[i-2][1]]
    for _ in range(N):
        case = int(input())
        print(dp[case][0],dp[case][1])

if __name__ == '__main__':
    main()
