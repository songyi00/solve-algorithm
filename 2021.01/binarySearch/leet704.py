def main():
    nums = list(map(int,input().split()))
    target = int(input())
    nums.sort()
    left = 0
    right = len(nums)

    while left<=right:
        mid = (left+right)//2
        if nums[mid]<target:
            left = mid+1
        elif nums[mid]>target:
            right = mid-1
        else:
            answer = mid
            print(answer)
            break
    
if __name__ == '__main__':
    main()