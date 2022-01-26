def main():
    N,C = map(int,input().split())
    locations = [int(input()) for _ in range(N)]
    locations.sort()
    left = float('inf')
    right = locations[-1]-locations[0] # 최대 거리 
    for i in range(len(locations)-1):
        left = min(locations[i+1]-locations[i],left) #최소 거리 
    
    answer = 0 

    while left <= right:
        mid = (left+right)//2 # 가장 인접한 공유기 사이의 거리 
        count = 1
        current = locations[0]
        for j in range(1,len(locations)):
            if locations[j]- current >=mid:
                current = locations[j]
                count += 1
        if count >= C : # 주어진 공유기 개수보다 많거나 같은 경우 
            answer = mid
            left = mid + 1 
        elif count < C : #주어진 공유기 개수보다 적은 경우 
            right = mid -1 

    print(right)

if __name__ == '__main__':
    main()

"""
공유기 설치 
가장 인접한 두 공유기 사이의 거리를 최대로 하는 프로그램 
""" 