import itertools
def main():
    perm = input().split()
    print(perm)
    print(list(itertools.permutations(perm)))
    print(list(itertools.combinations(range(1,4),2)))
if __name__ == "__main__":
    main()