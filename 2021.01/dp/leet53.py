import sys 
def main():
    int_list = list(map(int,input().split()))
    current_max = int_list[0]
    result = int_list[0]
    for i in range(1,len(int_list)):
        current_max = max(int_list[i],current_max+int_list[i])
        result = max(result,current_max)
    print(result)
    
if __name__ == "__main__":
    main()
"""
최대 서브 배열
합이 최대가 되는 연속 서브 배열을 찾아 합을 리턴하라.  
"""