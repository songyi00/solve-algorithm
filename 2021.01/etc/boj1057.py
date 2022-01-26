def main():
    n,a,b = map(int,input().split())
    group = [[i] for i in range(1,n+1)]
    round = 0
    flag = False
    while True:
        round += 1 
        for i in range(0,len(group)//2):
            if i+1 < len(group):
                group[i].extend(group[i+1])
                del group[i+1]
        for g in group:
            if a in g and b in g:
                flag = True
                break
        if flag:
            break
    #print(group)
    print(round)

if __name__ == "__main__":
    main()