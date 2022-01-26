from collections import defaultdict
def dfs(graph,start):
    stack = []
    visit = []
    stack.append(graph[start][0])

    while(stack):
        popNode = stack.pop()
        visit.append(popNode)
        count = 0 
        exist = False
        for v in graph[popNode]: 
            exist = True
            if v not in visit:
                count += 1
                stack.append(v)
        if exist and count == 0: 
            return False 
    return True


def main():
    graph = defaultdict(list)
    while True:
        try:
            a,b = input().split()
            graph[a].append(b)
        except :
            print(dfs(graph,a))
            exit()
            
if __name__ == "__main__":
    main()

    #그래프가 순환구조인지 판단 
    #갈 수 있는 경로가 이미 전부 방문한 경우 