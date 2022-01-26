from collections import defaultdict
import sys 
sys.setrecursionlimit(10**6)

longest = 0 

def dfs(tree,root):
    global longest

    if root =='.':
        return -1
    left = dfs(tree,tree[root][0])
    right = dfs(tree,tree[root][1])

    #가장 긴 경로(루트에서 왼쪽 상태값과 오른쪽 상태값을 더한 경로)
    #2를 더하는 것은 최상위 루트에서 왼쪽 오른쪽의 연결 거리 
    longest = max(longest,left+right+2)
    
    #상태값(리프노드로에서 현재 노드까지의 거리)
    return max(left,right) + 1

def main():
    N = int(input()) #정점 개수
    tree = defaultdict(list)
    parent_list = defaultdict(int)
    for _ in range(N):
        parent, left, right = input().split()
        tree[parent] = [left,right]
        parent_list[left] = parent
        parent_list[right] = parent 
    
    # 최상위 루트 찾는 방법 
    root = 0
    for k in tree.keys():
        if parent_list[k] == 0:
            root = k
            break

    dfs(tree,root)
    print(longest)

if __name__ == "__main__":
    main()

# 이진트리에서 두 노드 간 가장 긴 경로의 길이를 출력하라 