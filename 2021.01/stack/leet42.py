def main():
    height_list = list(map(int,input().split()))
    stack = []
    volume = 0
    for i in range(len(height_list)):
        while stack and height_list[i]>height_list[stack[-1]]:
            top = stack.pop()
            if not stack:
                break
            distance = i-stack[-1]-1 #거리차이 
            waters = min(height_list[stack[-1]],height_list[i]) - height_list[top]#물 높이 

            volume += distance*waters

        stack.append(i)

    print(volume)

if __name__ == "__main__":
    main()