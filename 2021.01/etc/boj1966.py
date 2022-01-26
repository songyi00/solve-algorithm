from collections import deque
def main():
    case = int(input())
    for _ in range(case):
        N , M = map(int,input().split()) #문서 개수, 궁금한 문서 위치 
        nums = list(map(int,input().split()))
        importance = deque()
        for i,e in enumerate(nums):
            importance.append((e,i))
        count = 0 
        while True:
            flag = True
            for num in importance:
                if importance[0][0] < num[0] :
                    temp = importance.popleft()
                    importance.append(temp)
                    flag = False
                    break
            if flag: # 인쇄가 되는 경우 
                temp = importance.popleft()
                count += 1
                if temp[1] == M: # 원하는 문서가 인쇄된 경우 
                    break
        print(count)
                
if __name__ == "__main__":
    main()