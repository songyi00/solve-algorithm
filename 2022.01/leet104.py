from collections import defaultdict,deque

"""
leet code 104번 
이진 트리의 최대 깊이 구하기
"""
def depth(root,tree):
    queue = deque([root])
    cnt = 0
    while queue:
        cnt+=1
        for i in range(len(queue)):
            cur_root = queue.popleft()
            for child in tree[cur_root]:
                if child != '.':
                    queue.append(child)
    return cnt
            
N = int(input()) # 노드 개수 
tree = defaultdict(list)
for i in range(N):
    root,left,right = input().split()
    tree[root].append(left)
    tree[root].append(right)

print(depth("3",tree))
    