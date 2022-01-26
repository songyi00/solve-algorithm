def main():
    money = 1000-int(input())
    count = 0 

    count += money//500
    money -= 500 * (money//500)
    count += money//100
    money -= 100 * (money//100)
    count += money//50
    money -= 50 * (money//50)
    count +=money//10
    money -= 10 * (money//10)
    count += money//5
    money -= 5 * (money//5)
    count += money//1
    money -= 1 * (money//1)
    print(count)

if __name__ == "__main__":
    main()
    # 잔돈 최소가 되는 매수 출력 