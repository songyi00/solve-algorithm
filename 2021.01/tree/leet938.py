from collections import defaultdict
def dfs(tree,root,L,R):
    stack = [root]
    sum = 0
    while stack:
        node = stack.pop()
        
        if node == '.':
            continue
        if node < L :
            stack.append(tree[node][1])
        elif node > R:
            stack.append(tree[node][0])
        else :
            sum += node
            stack.append(tree[node][0])
            stack.append(tree[node][1])
    return sum

def main():
    N = int(input())
    tree = defaultdict(list)
    for _ in range(N):
        parent,left,right = input().split()
        parent = int(parent)
        if left !='.':
            tree[parent].append(int(left)) 
        else :
            tree[parent].append(left)
        if right !='.':
            tree[parent].append(int(right))
        else:
            tree[parent].append(right)
    
    L,R = map(int,input().split())

    print(dfs(tree,10,L,R))

if __name__ == "__main__":
    main()

"""
이진 탐색 트리가 주어졌을 때 L이상 R이하 값을 지닌 노드의 합을 구하라
6
10 5 15
5 3 7
15 . 18
3 . .
7 . .
18 . .
7 15
"""