def main():
    numbers = list(map(int,input().split()))
    target = int(input())

    for i,num in enumerate(numbers):
        expected = target-num
        left, right = i, len(numbers)-1
        while left <= right :
            mid = (left+right)//2
            if numbers[mid] < expected:
                left = mid + 1
            elif numbers[mid] > expected:
                right = mid - 1
            else :
                print(i+1,mid+1)
                break
        
if __name__ == '__main__':
    main()
    
"""
두 수의 합 
정렬된 배열을 받아 덧셈하여 타겟을 만들 수 있는 배열의 두 숫자 인덱스를 리턴 
""" 