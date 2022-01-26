def main():
    N = int(input()) # 로프 개수 
    ropes = [int(input()) for _ in range(N)]
    ropes.sort()
    num = len(ropes)
    result = 0
    for i in range(len(ropes)):
        result = max(result,ropes[i]*num)
        num -= 1 
    print(result)
    
if __name__ == "__main__":
    main()