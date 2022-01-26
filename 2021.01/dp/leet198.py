def main():
    house_list = [0]+list(map(int,input().split()))
    dp = [0 for _ in range(len(house_list))]
    for i in range(1,len(house_list)):
        if i == 1:
            dp[i] = house_list[i]
            continue
        dp[i] = max(dp[i-1],dp[i-2]+house_list[i])

    print(dp[len(house_list)-1])

if __name__ == "__main__":
    main()

"""
한칸 이상 떨어진 집만 훔치는 것이 가능한 전문 털이범
훔칠 수 있는 가장 큰 금액을 출력하라. 
"""