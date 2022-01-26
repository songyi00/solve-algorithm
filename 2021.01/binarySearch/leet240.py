def main():
    matrix = [list(map(int,input().split())) for _ in range(5)]
    target  = int(input())
    print(any(target in row for row in matrix))

if __name__ == '__main__':
    main()
"""
2차원 행렬에서 원하는 타겟 존재하는지 검색하기
"""