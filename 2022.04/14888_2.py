
import sys

input = sys.stdin.readline 

maxi = -float('inf')
mini = float('inf')

def dfs(depth, total, plus, minus ,multiply, divide):
    global maxi, mini
    if depth == N :
        maxi = max(total,maxi)
        mini = min(total,mini)
        return
    
    if plus :
        dfs(depth+1, total+nums[depth],plus-1, minus, multiply,divide)
    if minus :
       dfs(depth+1, total-nums[depth],plus, minus-1, multiply,divide)
    if multiply:
        dfs(depth+1, total*nums[depth],plus, minus, multiply-1,divide)
    if divide:
        dfs(depth+1, int(total/nums[depth]),plus, minus, multiply,divide-1) 
    
N = int(input())
nums = list(map(int,input().split()))
ops = list(map(int,input().split()))

dfs(1,nums[0],ops[0], ops[1], ops[2], ops[3])
print(maxi)
print(mini)