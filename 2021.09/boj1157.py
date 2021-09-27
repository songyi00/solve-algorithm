from collections import defaultdict
temp = input().upper()
dic = defaultdict(int)

for t in temp:
    dic[t]+=1

val = 0
result = ''
cnt = 0
for k,v in dic.items():
    if val < v :
        result = k
        val = v 
        cnt = 0
    elif val == v:
        cnt+=1
if not cnt:
    print(result)
else:
    print('?')

#print(dic)