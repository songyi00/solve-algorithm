def main():
    candies = []
    n = int(input())
    for i in range(n):
        candies.append(int(input()))
    total = sum(candies)//2 #전체 사탕 개수 
    for i in range(n):
        temp = 0
        k = 0
        for _ in range(n//2): #더해야 하는 횟수 
            temp += candies[(i+1+k)%n]
            k += 2 
        print(total-temp)
        
if __name__ == "__main__":
    main()