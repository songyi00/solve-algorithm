def main():
    N = int(input()) # 지방 개수
    budgets = list(map(int,input().split()))
    totalBudget = int(input())
    left,right = 0,max(budgets)

    while left<=right:
        mid = (left+right)//2
        s = 0
        for b in budgets:
            if b>mid:
                s += mid
            else:
                s += b
        if s > totalBudget: # mid(상한액)이 너무 큰 경우 
            right = mid - 1
        else :
            left = mid + 1

    print(right)

if __name__ == '__main__':
    main()