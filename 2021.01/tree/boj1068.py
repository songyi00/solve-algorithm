from collections import defaultdict

count = 0 
def numOfLeaf(tree,root,removeNode):
    global count 
    depth_list = []
    if root == removeNode:
        return -1

    if len(tree[root]) >=2:
        for node in tree[root]:
            depth_list.append(numOfLeaf(tree,node,removeNode))
    elif len(tree[root]) == 1:
        depth_list.append(numOfLeaf(tree,tree[root][0],removeNode))
        if depth_list[0] == -1:
            count += 1
    else : 
        count+=1
        

def main():
    N = int(input())
    tree = defaultdict(list)
    parent_list = list(map(int,input().split()))
    root_list = []
    for i in range(N):
        if parent_list[i] != -1:
            tree[parent_list[i]].append(i)
        else:
            root_list.append(i)
    #print(tree)
    removeNode = int(input())
    sum = 0
    global count 
    for r in root_list:
        numOfLeaf(tree,r,removeNode)
        sum += count
        count = 0

    print(sum)

if __name__ == "__main__":
    main()