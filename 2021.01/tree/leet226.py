from collections import defaultdict,deque

def bfs(tree,root):
    queue = deque(root)
    while queue:
        node = queue.popleft()
        if node != '.':
            left, right = tree[node]
            tree[node] = [right, left]
            queue.append(left)
            queue.append(right)
    return tree

def main():
    N = int(input()) #정점 개수
    tree = defaultdict(list)
    parent_list = defaultdict(int)
    for _ in range(N):
        parent, left, right = input().split()
        tree[parent] = [left,right]
        parent_list[left] = parent
        parent_list[right] = parent 
    
    root = 0
    for k in tree.keys():
        if parent_list[k] == 0:
            root = k
            break

    print(bfs(tree,root))
    
if __name__ == "__main__":
    main()