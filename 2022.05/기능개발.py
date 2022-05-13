from collections import deque 
def solution(progresses, speeds):
    answer = []
    progresses = deque(progresses)
    shift = 0
    while progresses:
        cnt = 0
        for i in range(len(progresses)):
            progresses[i] += speeds[i+shift]
        
        for j in range(len(progresses)):
            if progresses[j] >= 100:
                cnt+=1
            else :
                break
        for _ in range(cnt):
            progresses.popleft()
        if cnt:
            answer.append(cnt)
        shift+=cnt
    return answer

progresses = list(map(int,input().split()))
speeds = list(map(int,input().split()))
print(solution(progresses, speeds))