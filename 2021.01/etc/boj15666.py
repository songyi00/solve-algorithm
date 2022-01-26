from itertools import combinations_with_replacement

#조합의 합 (중복조합)
def main():
    n, m = map(int,input().split())
    int_list = list(map(int,input().split()))
    int_list = sorted(list(set(int_list)))
    combi = list(combinations_with_replacement(int_list,m))

    for c in combi:
        print(*c)
        
if __name__ == "__main__":
    main()