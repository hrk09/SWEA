import sys
sys.stdin = open('input.txt', 'r')


TC = int(input())

for t in range(1, TC+1):
    # arr 받기
    row_arr = [list(map(int, input().split())) for i in range(9)]
    total = 45
    result = True

    # 가로줄 조사
    for row in row_arr:
        if sum(row) != total:
            result = False
            break

    # 세로줄 조사
    col_arr = list(map(list, zip(*row_arr)))
    for col in col_arr:
        if sum(col) != total:
            result = False
            break

    # 33 조사

    # 시작점 찾기
    for i in range(0, 9, 3):  # 0, 3, 6
        if result == True:
            for j in range(0, 9, 3):
                sum1 = 0  # 초기화
                # 시작점 기준 돌릴 범위 설정하기
                for x in range(3):
                    for y in range(3):
                        sum1 += row_arr[i + x][j + y]
                if sum1 != total:
                    result = False
                    break
                else:
                    result = True

    print('#{} {}'.format(t, int(result)))