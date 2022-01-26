def knapsack(w, weight_list, value_list):
    dp = [[0 for _ in range(w+1)] for _ in range(len(weight_list))]
    item_cnt = len(weight_list)

    for i in range(1,item_cnt): # 총 아이템 개수 
        for j in range(1,w+1): # 무게 제한 
            weight = weight_list[i] 
            value = value_list[i]
            if weight > j : # i번째 보석이 배낭의 무게 한도보다 무거운 경우 
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = max(dp[i-1][j-weight]+value , dp[i-1][j])
    return dp[item_cnt-1][w]
    
def main():
    w = int(input()) # 무게 제한 조건 
    n = int(input()) # 아이템 개수 
    input_weight = [0] + list(map(int,input().split())) # 무개 리스트 
    input_value = [0] + list(map(int,input().split())) # 가치 리스트 
    print(knapsack(w,input_weight,input_value))

if __name__ == "__main__":
    main()

"""
배낭 문제
가격이 최대가 되도록 item을 배낭에 담는 방법은? 

5
4
2 3 4 5
3 4 5 6 
"""