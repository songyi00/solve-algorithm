def main():
    graph = list(map(int,input().split()))
    
    result = 0 
    for i in range(len(graph)-1):
        if graph[i] < graph[i+1]:
            result += graph[i+1] - graph[i]
    print(result)

if __name__ == "__main__":
    main()

# 주식을 사고팔기 가장 좋은 시점
# 매번 단계마다 이익을 취하는 탐욕 구조 