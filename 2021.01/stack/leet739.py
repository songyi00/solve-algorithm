#일일 온도 
def main():
    temperture = list(map(int,input().split()))
    stack = []
    result = [0 for _ in range(len(temperture))]
    for i in range(len(temperture)):
        while stack and temperture[i]>temperture[stack[-1]]:
            result[stack[-1]]=i-stack[-1]
            stack.pop()        
        stack.append(i)
    print(result)

if __name__ == "__main__":
    main()