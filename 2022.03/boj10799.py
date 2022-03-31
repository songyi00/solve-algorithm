import sys

input = sys.stdin.readline 

input_list = list(input())

i, num, result = 0, 0, 0

while i < len(input_list):
    if input_list[i] == '(' and input_list[i+1] == ')':
        result += num
        i=i+2
        continue
    elif input_list[i] == '(':
        num += 1
    elif input_list[i] == ')':
        num -= 1
        result += 1 
    i+=1
    
print(result)