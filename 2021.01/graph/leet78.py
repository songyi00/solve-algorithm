import sys
sys.setrecursionlimit(10**6)

def dfs(index,path,nums,result):
    result.append(path)

    for i in range(index,len(nums)):
        dfs(i+1,path+[nums[i]],nums,result)

def main():
    nums = list(map(int,input().split()))
    result = []
    dfs(0,[],nums,result)    
    print(result)
    
if __name__ == "__main__":
    main()