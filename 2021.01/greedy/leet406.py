import heapq

def main():
    heap = [] 
    result = []
    while True:
        try:
            h,k = map(int,input().split())
            heapq.heappush(heap,[-h,k]) # 최대 힙 
        except:
            while heap:
                h,k = heapq.heappop(heap)
                result.insert(k,[-h,k])
            print(result)
            exit()

if __name__ == "__main__":
    main()