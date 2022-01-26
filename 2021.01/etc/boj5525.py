def main():
    N = int(input()) # O의 개수
    M = int(input()) # S의 길이
    S = input() # 문자열 

    i = 0
    pattern = 0
    result = 0
    while i < M-2:
        if S[i]=='I' and S[i+1]=='O' and S[i+2] =='I':
            pattern+=1
            i+=1
            if pattern == N:
                pattern -= 1
                result +=1
        else:
            pattern = 0
        i+=1
                
    print(result)    

if __name__ == "__main__":
    main()