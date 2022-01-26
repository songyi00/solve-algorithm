def main():
    children = list(map(int,input().split())) # 아이들이 원하는 최소 쿠키 리스트 
    cookies = list(map(int,input().split())) # 줄 수 있는 쿠키 리스트 
    children.sort()
    cookies.sort()

    children_i , cookies_i = 0,0
    while children_i <len(children) and cookies_i < len(cookies):
        if children[children_i] <= cookies[cookies_i]: # 아이에게 쿠키를 줄 수 있는 경우 
            children_i += 1
        cookies_i += 1
    print(children_i)

if __name__ == "__main__":
    main()
# 그리디 