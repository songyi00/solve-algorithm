from collections import defaultdict,deque
visit = defaultdict(lambda : False)
def bfs(graph,start):
    result = []
    queue = deque([start])
    while queue:
        node = queue.popleft()
        visit[node] = False # dfs 이후이므로 반대로 setting 
        result.append(node)
        for v in graph[node]:
            if visit[v] and v not in queue:
                queue.append(v)
    return result

def dfs(graph,start):
    print(start,end=' ')
    visit[start] = True 
    for v in graph[start]:
        if not visit[v]:
            dfs(graph,v)

def main():
    N, M, V = map(int,input().split()) #정점 개수, 간선 개수, 탐색 시작 번호 
    graph = defaultdict(list)
    for _ in range(M):
        u,v = map(int,input().split())
        graph[u].append(v)
        graph[v].append(u)
    for k in graph.keys():
        graph[k].sort()
        
    dfs(graph,V)
    print()
    print(*bfs(graph,V))

if __name__ == '__main__':
    main()