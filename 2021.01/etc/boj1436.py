def main():
    N = int(input())
    base = 666
    
    count = 0
    while True: 
        if '666' in str(base):
            count +=1
            if count == N:
                print(base)
                break
        base += 1
        
if __name__ == "__main__":
    main()

# 666을 포함하는 숫자중에 N번째로 작은 숫자