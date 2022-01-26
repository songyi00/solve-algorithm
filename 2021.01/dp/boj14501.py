def main():
    N = int(input())
    time_list = [0]
    price_list = [0]
    for _ in range(N):
        t,p = map(int,input().split())
        time_list.append(t)
        price_list.append(p)
    dp = [0 for _ in range(N+1)]
    current = 0
    for i in range(N,0,-1):
        time = time_list[i]
        price = price_list[i]
        if i+time-1 <= N : # 상담을 잡을 수 있는 경우 
            #상담 잡을지 or 안 잡을지
            if i+time >= len(dp):
                dp[i] = max(price,current)
                current = dp[i]
            else : 
                dp[i] = max(dp[i+time]+price,current)
                current = dp[i]
        else : # 상담을 잡을 수 없는 경우 
            dp[i] = current

    print(dp[1])

if __name__ == '__main__':
    main()