tc = int(input())
for _ in range(tc):
    keylogger = list(input())
    left,right = [],[]  
    curser = 0 
    for log in keylogger:
        if log == '<':
            if left:
                right.append(left.pop())
        elif log == '>':
            if right:
                left.append(right.pop())
        elif log == '-':
            if left:
                left.pop()
        elif log.isalpha:
            left.append(log)    

    print(''.join(left)+''.join(reversed(right)))

"""
insert(인덱스,값) 의 경우 시간복잡도가 선형시간 걸린다. 
즉 직관적으로 풀기보다는 생각의 전환이 필요
문자열을 기준으로 커서를 옮기지말고 커서를 기준으로 문자열을 옮겨
pop과 append만을 사용해서 구현하자!!  
"""

