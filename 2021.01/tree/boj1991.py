import sys
sys.setrecursionlimit(10**6)
def preorder(tree,root): # 루트 왼 오
    if root =='.':
        return
    print(root,end='')
    preorder(tree,tree[root][0])
    preorder(tree,tree[root][1])

def inorder(tree,root): #왼 루트 오
    if root =='.':
        return
    inorder(tree,tree[root][0])
    print(root,end='')
    inorder(tree,tree[root][1])

def postorder(tree,root): # 왼 오 루트 
    if root =='.':
        return
    postorder(tree,tree[root][0])
    postorder(tree,tree[root][1])
    print(root,end='')
    
def main():
    N = int(input())
    tree = {}
    for _ in range(N):
        parent, left, right = input().split()
        tree[parent]=[left,right]
    preorder(tree,'A')
    print()
    inorder(tree,'A')
    print()
    postorder(tree,'A')

if __name__ == "__main__":
    main()