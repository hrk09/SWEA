'''
10
4 5 7 1 6 3 8 2 9
6 3 9 8 2 7 5 4 1
7 9 3 4 8 5 1 6 2
1 8 2 5 4 9 6 3 7
8 6 1 7 9 2 3 5 4
5 2 4 6 3 1 7 9 8
3 7 6 9 1 4 2 8 5
2 4 5 3 7 8 9 1 6
9 1 8 2 5 6 4 7 3
'''
import sys
sys.stdin = open('input.txt', 'r')

for T in range(1, int(input())+1):
    total = 45
    result = True
    N = 9
    
    # 행조사
    row_lst = list(list(map(int, input().split())) for i in range(N))
    for r in row_lst:
        if sum(r) != 45:
            result = False 
            break
    
    if result:  # 만약 result 가 1이라면,
        #열조사
        col_lst = list(map(list, zip(*row_lst)))
        for c in col_lst:
            if sum(c) != 45:
                result = False 
                break
    
    # 가로줄 3행씩 조사
    if result:
        k = 0
        l = 0
        arr = []
        for i in range(k, k + 3):
            for j in range(l, l + 3):
                arr.append(row_lst[i][j])
        # print(arr)  # [4, 5, 7, 6, 3, 9, 7, 9, 3]
        if sum(arr) != total:
            result = False
        else:
            arr = []  # 다시 빈 리스트로 초기화
            k = 0  # range 초기화
            l += 3  # 열 범위 + 해주기
        if l > 9:  # 열 길이가 9 이상이 되면, result 는 1이고, 다음 단계로 넘어가기!
            result = True
            k += 3  # 행 범위 + 해주기


    print('#{} {}'.format(T, int(result)))