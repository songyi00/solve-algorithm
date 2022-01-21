from collections import defaultdict,deque
from multiprocessing import parent_process
"""
leetcode 543번
이진트리의 직경 
"""

longest = 0
def find_max_length(tree, root): # 재귀 
    global longest
    
    if root == '.':
        return -1 
    
    left = find_max_length(tree,tree[root][0])
    right = find_max_length(tree,tree[root][1])
    
    longest = max(longest, left+right+2) # 거리
    
    return max(left,right)+1 # 상태값(left와 right도 마찬가지로 상태값)
    
    
tree = defaultdict(list)
parent = defaultdict(int)

N = int(input())
for _ in range(N):
    root, left, right = input().split()
    tree[root] = [left,right]
    parent[left] = root
    parent[right] = root

find_root = 0
for k in tree.keys():
    if parent[k] == 0:
        find_root = k
        break
    
find_max_length(tree, find_root)
print(longest)
