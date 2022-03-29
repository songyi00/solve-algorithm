non_self_list = []

def isSelfNumber(num):
    for s in list(str(num)):
        num += int(s)
    non_self_list.append(num)


for i in range(1,10001):
    isSelfNumber(i)

for j in range(1,10001):
    if j not in non_self_list:
        print(j)