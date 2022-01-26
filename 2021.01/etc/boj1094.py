import heapq

def main():
    stick = []
    answer = int(input())
    heapq.heappush(stick,64)
   
    while answer!=64:
        num = heapq.heappop(stick)
        half = num//2 
    
        if half == 0:
            break
        elif half > answer: # 절반 중 하나 버리기 
            heapq.heappush(stick,half)
        elif half < answer:                 
            heapq.heappush(stick,half)   
            heapq.heappush(stick,half)
        else:
            heapq.heappush(stick,half)
            break
    stick = sorted(stick)
    result = []
    
    for s in stick[::-1]:
        result.append(s)
        compare = sum(result)
        if compare == answer:
            break
        elif compare > answer:
            result.pop()
    print(len(result))


if __name__ == "__main__":
    main()