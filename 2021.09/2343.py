import sys
input = sys.stdin.readline 

n,m = map(int,input().split())
times = list(map(int,input().split()))

left,right = 0, sum(times)

while left<=right:
    mid = (left+right)//2 #가능한 블루레이의 최소 크기 
    val = 0
    divide = [] 
    for time in times:
        val += time
        if val > mid:
            divide.append(val-time)
            val=time
    if val:
        divide.append(val)
        
    if max(divide) > mid : # 예외처리 (mid보다 구분할 값이 더 큰 경우)
        left = mid + 1
    elif len(divide) <= m: # mid가 더 작아져야 함 
        right = mid - 1
        result = mid 
    else: # mid가 더 커져야 함 
        left = mid + 1
    
print(result)


