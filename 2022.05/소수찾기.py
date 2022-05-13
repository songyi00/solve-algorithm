from collections import defaultdict

from numpy import number
numbers = list(input())
array = []
cnt = 0
visit = defaultdict(lambda:False)
find = defaultdict(lambda:False)

def check(num):
    for i in range(2,num):
        if num%i == 0:
            return False
    return True
    
def dfs(n,depth):
    global array, cnt
    if n == depth:
        print(array)
        temp = int("".join(array))
        if check(temp) and not visit[temp]:
            cnt +=1
        visit[temp] = True
        return
    for i in range(depth):
        if not find(numbers[i]):
            array.append(numbers[i])
            dfs(k+1,n+1,depth)
            array.pop()

dfs(0,0,len(numbers))
print(cnt)