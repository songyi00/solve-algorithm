import itertools 
def main():
    N = int(input())
    tip_list = [int(input()) for _ in range(N)]
    tip_list = sorted(tip_list)[::-1]
    sum = 0
    for i in range(1,N+1):
        if tip_list[i-1]-(i-1) > 0:
            sum += tip_list[i-1]-(i-1)
    print(sum)
if __name__ == "__main__":
    main()