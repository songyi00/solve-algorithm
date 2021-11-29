x,y = map(int,input().split())
z = (y*100)//x

left,right = 0,1000000000

result = 0
while left<=right:
    mid = (left+right)//2
    new_z = (y+mid)*100//(x+mid)
    if z!=new_z: # z 변함 
        right = mid -1
        result = mid
    else: # 변하지 않음 
        left = mid + 1
    
if result:
    print(result)
else:
    print(-1)