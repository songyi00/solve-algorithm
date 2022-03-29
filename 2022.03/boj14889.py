import itertools
import sys
input = sys.stdin.readline

def calculate_score(groupA,groupB):
    sum_a = 0
    sum_b = 0
    for a in itertools.combinations(groupA,2):
        sum_a += (skill_matrix[a[0]][a[1]] + skill_matrix[a[1]][a[0]])
    for b in itertools.combinations(groupB,2):
        sum_b += (skill_matrix[b[0]][b[1]] + skill_matrix[b[1]][b[0]])
    
    return abs(sum_a-sum_b)
      
skill_matrix = []

N = int(input())
for _ in range(N):
    skill_matrix.append(list(map(int,input().split())))    

pool = [i for i in range(N)]
current = float('inf')

for groupA in itertools.combinations(pool,N//2):
    groupA = list(groupA)
    groupB = []
    for j in range(N):
        if j not in groupA:
            groupB.append(j)
    interval = calculate_score(groupA,groupB)
    current = min(interval,current)

print(current)