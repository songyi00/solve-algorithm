import re
def main():
    calculate = input().split('-')
    calculate_list = [] 
    for c in calculate:
        sub = 0 
        substr = c.split('+')
        for num in substr:
            sub+=int(num)
        calculate_list.append(sub)
    result = calculate_list[0]
    for i in range(1,len(calculate_list)):
        result -= calculate_list[i]
    print(result)


if __name__ == "__main__":
    main()
