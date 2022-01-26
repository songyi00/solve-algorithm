def main():
    N = int(input())
    bulk = []
    for _ in range(N):
        x, y = map(int,input().split())
        bulk.append((x,y))

    for p,q in bulk:
        rank = 1
        for a,b in bulk:
            if p<a and q<b:
                rank += 1 
        print(rank,end=' ')
    
if __name__ == "__main__":
    main()