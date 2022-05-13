from itertools import permutations
from collections import defaultdict

def check(num):
    if num <= 1:
        return False
    for i in range(2,num):
        if num%i == 0:
            return False
    return True

str_list = list(input())
visit = defaultdict(lambda:False)
cnt = 0

for j in range(1,len(str_list)+1):
    for pool in permutations(str_list,j):
        # print(pool)
        num = int(''.join(list(pool)))
        if check(num) and not visit[num]:
            visit[num] = True
            cnt+=1
print(cnt)