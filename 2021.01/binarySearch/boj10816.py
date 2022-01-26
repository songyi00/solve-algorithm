from collections import defaultdict
def main():
    N = int(input())
    cards = list(map(int,input().split()))
    M = int(input())
    nums = list(map(int,input().split()))
    dic = defaultdict(int)
    for card in cards:
        dic[card]+=1
    for num in nums:
        print(dic[num],end=' ')

if __name__ == '__main__':
    main()
