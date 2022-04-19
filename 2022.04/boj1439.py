import sys
input = sys.stdin.readline 

str_list = list(input().strip())
check = str_list[0]
flag = False
cnt = 0
for i in range(len(str_list)):
    if str_list[i] != check:
        if not flag:
            cnt += 1
            flag = True
    else:
        if flag : 
            flag = False
            
print(cnt)     