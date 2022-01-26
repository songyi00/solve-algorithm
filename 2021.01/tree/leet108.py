from collections import defaultdict

def sortedArrayToBst(sorted_list,tree):
    if not sorted_list:
        return None 

    mid = len(sorted_list)//2
    node = sorted_list[mid]

    tree[node].append(sortedArrayToBst(sorted_list[:mid],tree)) # 왼쪽
    tree[node].append(sortedArrayToBst(sorted_list[mid+1:],tree)) # 오른쪽 

    return node

def main():
    sorted_list = list(map(int,input().split()))
    tree = defaultdict(list)
    sorted_list.sort()
    sortedArrayToBst(sorted_list,tree)

    print(tree)

if __name__ == "__main__":
    main()

#정렬된 배열의 이진 탐색 트리 변환(재귀 이용)