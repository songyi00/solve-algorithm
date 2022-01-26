def main():
    string = list(input())
    print(''.join(sorted(list(set(string)))))

if __name__ == "__main__":
    main()