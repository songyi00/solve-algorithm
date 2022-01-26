from collections import defaultdict,deque
def bfs(tree,root):
    queue = deque()
    queue.append(root)
    visit = defaultdict(lambda : False)
    parent = defaultdict(int)

    while queue:
        node = queue.popleft()
        visit[node] = True
        for n in tree[node]:
            if not visit[n]:
                queue.append(n)
                parent[n]= node
    return parent

def main():
    tree = defaultdict(list)
    N = int(input())
    for _ in range(N-1):
        a , b = map(int,input().split())
        tree[a].append(b)
        tree[b].append(a)
    parent = bfs(tree,1)
    
    for i in range(2,N+1):
        print(parent[i])

if __name__ == "__main__":
    main()

    # 트리의 부모 노드 출력 