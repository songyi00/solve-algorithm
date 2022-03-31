N = int(input())
road_length = list(map(int,input().split()))
price = list(map(int,input().split()))

min_val = price[0]
sum = 0
for i in range(N-1):
    if price[i] < min_val:
        min_val = price[i] 
    sum += (road_length[i]*min_val)
    
print(sum)