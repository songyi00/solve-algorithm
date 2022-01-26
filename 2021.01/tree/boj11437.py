from collections import defaultdict,deque
def lca(route1,route2):
    i = 0
    end = min(len(route1),len(route2))
    while i!=end:
        if route1[i] != route2[i]:
            break
        i+=1
    return route1[i-1]

def bfs(tree,root,parent_list): # 각 노드의 부모 알아냄 
    queue = deque([root])
    visit = defaultdict(lambda : False)
    while queue:
        node = queue.popleft()
        visit[node] = True
        for v in tree[node]:
            if not visit[v]:
                parent_list[v] = node
                queue.append(v)
    return parent_list 

def main():
    N = int(input()) # 정점 개수 
    tree = defaultdict(list)
    parent_list = defaultdict(int)
    
    for _ in range(N-1):
        a,b = map(int,input().split())
        tree[a].append(b)
        tree[b].append(a)

    parent_list = bfs(tree,1,parent_list)

    M = int(input())
    for _ in range(M): 
        target1,target2 = map(int,input().split())
        route1 = deque([target1])
        route2 = deque([target2]) 

        while parent_list[target1]:
            route1.appendleft(parent_list[target1])
            target1 = parent_list[target1]
        while parent_list[target2]:
            route2.appendleft(parent_list[target2])
            target2 = parent_list[target2]

        print(lca(route1,route2))

if __name__ == "__main__":
    main()
    #가장 가까운 공통 조상 
    #루트는 1 