def main():
    while True:
        N = int(input())
        if N == 0:
            break
        else:
            word_list = []
            for _ in range(N):
                word_list.append(input())
            word_list.sort(key = lambda x: x.lower())
            print(word_list[0])

if __name__ == '__main__':
    main()