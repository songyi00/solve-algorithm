def main():
    num = int(input())
    dp = [i for i in range(num+1)]
    
    for i in range(1,num+1):
        j = 1
        while j*j <=i :
            if dp[i] > dp[i-j*j] + 1:
                dp[i] = dp[i-j*j]+1
            j+=1
    
    print(dp[num])
if __name__ == "__main__":
    main()
