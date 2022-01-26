from collections import defaultdict

mergeTree = defaultdict(list)

def mergeBinaryTree(tree1,tree2,start1,start2):
    global mergeTree
    if start1!='.' and start2 !='.':
        node = start1 + start2
        mergeTree[start1+start2].append(mergeBinaryTree(tree1,tree2,tree1[start1][0],tree2[start2][0]))#left
        mergeTree[start1+start2].append(mergeBinaryTree(tree1,tree2,tree1[start1][1],tree2[start2][1]))#right 
    else:
        if start1=='.':
            start1 = 0
        if start2 =='.':
            start2 = 0
        node = start1 + start2
    return node

def main():
    n1,n2 = map(int,input().split()) #각 트리의 정점 개수 
    tree1 = defaultdict(list)
    tree2 = defaultdict(list)

    for _ in range(n1):
        parent,left,right = input().split()
        parent = int(parent)
        if left !='.':
            tree1[parent].append(int(left))
        else :
            tree1[parent].append(left)
        if right !='.':
            tree1[parent].append(int(right))
        else:
            tree1[parent].append(right)

    for _ in range(n2):
        parent,left,right = input().split()
        parent = int(parent)
        if left !='.':
            tree2[parent].append(int(left))
        else :
            tree2[parent].append(left)
        if right !='.':
            tree2[parent].append(int(right))
        else:
            tree2[parent].append(right)

    mergeBinaryTree(tree1,tree2,1,2)
    print(mergeTree)

if __name__ == "__main__":
    main()

#두 이진트리의 병합 (재귀 사용)

"""
5 5
1 3 2
3 5 .
2 . .
5 6 .
6 . .
2 1 3
1 . 4
3 . 7
4 . .
7 . .
"""