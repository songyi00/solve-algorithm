from collections import deque
def main():
    card_list = deque()
    num = int(input())
    for i in range(1,num+1):
        card_list.append(i)
    i = 0
    while len(card_list)!=1:
        if i%2 ==0:
            card_list.popleft()
        else:
            card_list.append(card_list.popleft())
        i+=1
    print(card_list[0])

if __name__ == "__main__":
    main()