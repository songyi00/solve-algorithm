from collections import defaultdict
def heightBalanced(tree,root):
    if root =='.':
        return 0

    left = heightBalanced(tree,tree[root][0])
    right = heightBalanced(tree,tree[root][1])

    if abs(left-right) > 1 or left == -1 or right == -1:
        return -1
    else :
        return max(left,right)+1

def main():
    N = int(input()) #정점 개수
    tree = defaultdict(list) 
    parent_list = defaultdict(int)

    for _ in range(N):
        parent,left,right = input().split()
        parent = int(parent)
        if left !='.':
            tree[parent].append(int(left))
            parent_list[left]= parent
        else :
            tree[parent].append(left)
        if right !='.':
            tree[parent].append(int(right))
            parent_list[right] = parent
        else:
            tree[parent].append(right)

    
    root = 0
    for k in tree.keys():
        if parent_list[k] ==0:
            root = k
            break 
    
    result = heightBalanced(tree,root)
    if result>=0:
        print(True)
    else:
        print(False)

if __name__ == "__main__":
    main()

# 균형이진트리(Height Balanced Tree)
# 서브트리간의 최대 높이 차이는 1이다.
"""
7
1 2 3
2 4 5
4 6 7
3 . .
5 . .
6 . .
7 . .
"""