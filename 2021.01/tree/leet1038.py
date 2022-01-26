from collections import defaultdict,deque

add = 0
result = deque()
def bstToBig(tree, root): # 오 루트 왼 
    global add 
    if root == '.':
        return 0 
    add = root
    add += bstToBig(tree,tree[root][1])
    result.appendleft(add)
    add += bstToBig(tree,tree[root][0])

    return add 

def main():
    tree = defaultdict(list)
    N = int(input())
    for _ in range(N):
        parent,left,right = input().split()
        parent = int(parent)
        if left!='.':
            tree[parent].append(int(left))
        else:
            tree[parent].append(left)
        if right!='.':
            tree[parent].append(int(right))
        else:
            tree[parent].append(right)
    bstToBig(tree, 4)
    print(result)
if __name__ == "__main__":
    main()

"""
이진 탐색 트리를 더 큰 수 합계 트리로 
각 노드를 현재값보다 더 큰 값을 가진 모든 노드의 합으로 만들어라
9
4 1 6
1 0 2
6 5 7
0 . .
2 . 3
5 . .
7 . 8
8 . .
3 . .
"""