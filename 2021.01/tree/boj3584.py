from collections import defaultdict,deque
def lca(route1,route2):
    i = 0
    end = min(len(route1),len(route2))
    while i!=end:
        if route1[i] != route2[i]:
            break
        i+=1
    return route1[i-1]

def main():
    T = int(input()) #테스트 케이스
    for _ in range(T):
        tree = defaultdict(list)
        parent_list = defaultdict(int)
        N = int(input()) #정점 개수 
        for _ in range(N-1):
            parent,child = map(int,input().split())
            tree[parent].append(child)
            parent_list[child] = parent
            
        target1, target2 = map(int,input().split())
        route1 = deque([target1])
        route2 = deque([target2])

        while parent_list[target1]:
            route1.appendleft(parent_list[target1])
            target1 = parent_list[target1]
        
        while parent_list[target2]:
            route2.appendleft(parent_list[target2])
            target2 = parent_list[target2]
        #print(route1)
        #print(route2)
        print(lca(route1,route2))

if __name__ == "__main__":
    main()
    #가장 가까운 공통 조상 