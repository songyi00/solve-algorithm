def main():
    nums1 = list(map(int,input().split()))
    nums2 = list(map(int,input().split()))
    
    print(set(nums1)&set(nums2))

if __name__ == '__main__':
    main()

# 두 배열의 교집합 