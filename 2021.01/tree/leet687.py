from collections import defaultdict

count = 0 
def dfs(tree,root):
    global count 

    if root =='.':
        return 
    left = dfs(tree,tree[root][0])
    right = dfs(tree,tree[root][1])

    if left == root:
        left+=1
    else :
        left = 0
    
    if root != right:
        right +=1
    else:
        right = 0 

    count = max(count,left+right)
    return root

def main():
    N = int(input())
    tree = defaultdict(list)
    parent_list = defaultdict(int)

    for _ in range(N):
        parent,left,right = input().split()
        tree[parent]= [left,right]
        parent_list[left] = parent
        parent_list[right] = parent

    root = 0
    for k in tree.keys():
        if parent_list[k] == 0:
            root = k
            break
    print(dfs(tree,root))

if __name__ == "__main__":
    main()

#가장 긴 동일 값의 경로 