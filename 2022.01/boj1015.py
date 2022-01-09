N = int(input())
A = list(map(int,input().split()))

P = []
sorted_A = sorted(A)
for i in range(len(sorted_A)):
    idx = sorted_A.index(A[i])
    sorted_A[idx]= -1
    P.append(idx)
        
print(*P)