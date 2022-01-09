n = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

sorted_A = sorted(A)
sorted_B = sorted(B,reverse=True)

s = 0
for i in range(len(sorted_A)):
    s+= (sorted_A[i]*sorted_B[i])
print(s)
