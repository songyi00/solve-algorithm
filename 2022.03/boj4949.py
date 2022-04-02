import sys

input = sys.stdin.readline 

while True:
    s = input()
    if s[0] == '.':
        break
    str_list = list(s)
    stack = []
    flag = True
    for i in str_list:
        if i == '(' or i == '[':
            stack.append(i)
        elif i == ')':
            if not stack:
                flag = False
                break
            elif stack[-1] != '(':
                flag = False
                break
            else:
                stack.pop()
        elif i == ']':
            if not stack:
                flag = False
                break
            elif stack[-1] != '[':
                flag = False
                break
            else:
                stack.pop()
    if stack:
        flag = False
    if flag:
        print('yes')
    else:
        print('no')

