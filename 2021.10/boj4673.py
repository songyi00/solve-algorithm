nums = [0]*10001

for i in range(1,10001):
    cnt = 0
    for j in str(i):
        cnt += int(j)
    cnt += i
    if cnt <=10000:
        nums[cnt]=1    

for k in range(1,10001):
    if nums[k] == 0:
        print(k)