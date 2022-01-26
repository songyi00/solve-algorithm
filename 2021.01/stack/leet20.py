#유효한 괄호 판단 
def main():
    bracket = list(input())
    stack = []
    dic = {')':'(' , '}':'{', ']':'['}
    for b in bracket:
        if not stack:
            stack.append(b)
        elif b ==')' or b=='}' or b ==']' and stack[-1]==dic[b]:
            stack.pop()
        else :
            stack.append(b)
    
    if not stack:
        print("YES")
    else:
        print("NO")
        
if __name__ == "__main__":
    main()