from collections import defaultdict
import sys
sys.setrecursionlimit(10**6)

visit = [] 

def dfs(graph,start,result):
    result.append(start)
    while graph[start]:
        popNode = graph[start].pop(0)
        result = dfs(graph,popNode,result)
    return result

def main():
    graph = defaultdict(list)
    while True:
        try:
            a,b = input().split()
            graph[a].append(b)
        except:
            result = []
            for a in graph:
                graph[a].sort()
            result = dfs(graph,"JFK",result)
            print(result)
            exit()

if __name__ == "__main__":
    main()

"""
JFK에서 출발하는 여행 일정을 구해라 

MUC LHR
JFK MUC
SFO SJC
LHR SFO
"""