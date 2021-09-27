variable = input() 
result = []
stat = True
if '_' in variable: # c++ 형식 -> java 
    if variable[0] == '_':
        print('Error!')
        stat = False
    elif variable[-1] == '_':
        print('Error!')
        stat = False
    else:
        space = False
        for i in range(len(variable)):
            if variable[i].isupper(): 
                print('Error!')
                stat = False
                break
            elif variable[i] == '_':
                if i+1 <len(variable) and variable[i+1]=='_':
                    print('Error!')
                    stat = False
                    break
                space = True
            else: 
                if space:
                    result.append(variable[i].upper())
                    space = False
                else:
                    result.append(variable[i])
else: # java 형식 -> c++
    if variable[0].isupper():
        print('Error!')
        stat = False
    else:
        for i in range(len(variable)):  
            if variable[i].isupper():
                result.append('_')
                result.append(variable[i].lower())
            else:
                result.append(variable[i])

if stat:
    print(''.join(result))

"""
예외처리가 중요한 문제!!
먼저 예외처리할 조건 전부 적어놓고 시작하기
<java 형식인지 c++ 형식인지 먼저 구분 후>
- 대문자로 시작하는 경우 
- 대문자와 '_' 가 공존하는 경우 
- '_'로 시작하거나 끝나는 경우 
- etc .. 전부 적기 
"""