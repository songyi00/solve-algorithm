m,n = map(int,input().split())

alpha = ['zero','one','two','three','four','five','six','seven','eight','nine']
dic = {}
for i in range(m,n+1):
    num = str(i)
    s = ''
    for n in num:
        s+=alpha[int(n)]
    dic[s] = i

vals = [] 
for k,v in dic.items():
    vals.append((v,k))
vals.sort(key= lambda x: x[1])

for i in range(len(vals)):
    if i%10==0 and i!=0:
        print()
    print(vals[i][0],end=' ')

    
