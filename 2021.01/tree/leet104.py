from collections import defaultdict,deque
def depth(tree,root):
    queue = deque()
    queue.append((root,1))
    visit = []
    count = 1
    while queue: #while문을 돌리는 만큼 깊이 증가 
        v, count= queue.popleft()
        visit.append(v)
        for node in tree[v]:
            if node != '.' and node not in visit:
                queue.append((node,count+1))
    
    return count 

def main():
    N = int(input()) # 노드 개수
    tree = defaultdict(list) 
    parent = defaultdict(int)

    for _ in range(N):
        root,left,right = input().split()
        tree[root].append(left)
        tree[root].append(right)
        parent[left]= root
        parent[right] = root
    
    #트리 루트 구하기 
    root = ''
    for t in tree.keys():
        if parent[t]==0:
            root = t
            break
    
    print(depth(tree,root))

if __name__ == "__main__":
    main()