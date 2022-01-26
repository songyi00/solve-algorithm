def main():
    gas = list(map(int,input().split()))
    cost = list(map(int,input().split()))

    if sum(gas) < sum(cost):
        print(-1)
        exit() 
    
    fuel = 0 #남은 연료 
    start = 0 #시작 위치 
    for i in range(len(gas)):
        if gas[i] + fuel < cost[i]: # 출발점이 될 수 없는 경우 
            start = i+1 
            fuel = 0
        else:
            fuel += gas[i] - cost[i]
    print(start)
        
if __name__ == "__main__":
    main()

#주유소 방문 