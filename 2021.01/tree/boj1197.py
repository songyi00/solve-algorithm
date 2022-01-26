from collections import defaultdict,deque
import heapq
def prim(tree,start):
    queue = []
    visit = defaultdict(lambda : False)
    heapq.heappush(queue,(0,start)) # 비용, 노드 
    sum = 0 

    while queue:
        weight, node = heapq.heappop(queue)
        if visit[node]: #큐에 같은 노드가 여러번 들어가있을 수 있으므로 한번 더 체크 필수
            continue
        else :
            visit[node] = True
            sum += weight
        
        for nextV in tree[node]: # 다음노드, 비용 
            if not visit[nextV[0]]:
                heapq.heappush(queue,(nextV[1],nextV[0]))
    return sum 

def main():
    tree = defaultdict(list)
    V,E = map(int,input().split())
    for _ in range(E):
        a,b,c= map(int,input().split())
        tree[a].append([b,c])
        tree[b].append([a,c])
    print(prim(tree,1))

if __name__ == "__main__":
    main()

#프림