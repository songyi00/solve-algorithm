import itertools
import sys
input = sys.stdin.readline 

def calculate(pool):
    i = 1
    result = int_list[0]
    for p in range(len(pool)):
        if pool[p] =='+':
            result += int_list[i]
        elif pool[p] == '-':
            result -= int_list[i]
        elif pool[p] == 'x':
            result *= int_list[i]
        else:
            if int_list[i]* result >= 0:
                result = result//int_list[i]
            else:
                result = -(abs(result)//abs(int_list[i]))
        i += 1
    return result
N = int(input())
int_list = list(map(int,input().split()))
num_list = list(map(int,input().split()))

op_list = []
dic = dict()
dic[0] = '+'
dic[1] = '-'
dic[2] = 'x'
dic[3] = '/'
for i in range(4):
    if num_list[i] > 0:
        for j in range(num_list[i]):
            op_list.append(dic[i])

final_result = []
for pool in itertools.permutations(op_list):
    final_result.append(calculate(list(pool)))

print(max(final_result))
print(min(final_result))
