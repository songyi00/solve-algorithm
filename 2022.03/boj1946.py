import sys
input = sys.stdin.readline

tc = int(input())

for _ in range(tc):
    applicant_list = []
    n = int(input())
    for _ in range(n):
        s, m = map(int,input().split())
        applicant_list.append([s,m])
    applicant_list.sort()
    min_m = applicant_list[0][1] 
    cnt = 1
    for i in range(1,n):
        if applicant_list[i][1] <= min_m :
            min_m = applicant_list[i][1]
            cnt +=1
    print(cnt)
