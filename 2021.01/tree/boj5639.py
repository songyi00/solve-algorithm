from collections import defaultdict

def makeTree(vertices,binarySearchTree):
    if not vertices:
        return None 

    mid = len(vertices)//2
    
    node = vertices[mid] #루트 
    binarySearchTree[node].append(makeTree(vertices[:mid],binarySearchTree))
    binarySearchTree[node].append(makeTree(vertices[mid+1:],binarySearchTree))

    return node 

def main():
    preorderList = []
    binarySearchTree = defaultdict(list)
    while True:
        try:
            node = int(input())
            preorderList.append(node)
        except:
            makeTree(sorted(preorderList),binarySearchTree)
            print(binarySearchTree)
            exit()
if __name__ == "__main__":
    main()