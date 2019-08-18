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
    # 3x3 조사(1)
        split_lst = []
        j = 0
        for i in range(3):
            j = 0  # 초기화
            for c in range(N):  # 횟수
                split_lst.append(row_lst[i][j:j+3])
                j += 3
                if j > 6:
                    break
        # print(split_lst)

        # 판별(1)
        arr1 = list(split_lst[0] + split_lst[3] + split_lst[6])
        arr2 = list(split_lst[1] + split_lst[4] + split_lst[7])
        arr3 = list(split_lst[2] + split_lst[5] + split_lst[8])
        if sum(arr1) != total or sum(arr2) != total or sum(arr3) != total:
            result = False 

    if result:
    # 3x3 조사(2)
        split_lst = []
        j = 0
        for i in range(3):
            j = 0
            for c in range(N):
                split_lst.append(row_lst[i+3][j:j+3])
                j += 3
                if j > 6:
                    break

        # 판별(2)
        arr1 = list(split_lst[0] + split_lst[3] + split_lst[6])
        arr2 = list(split_lst[1] + split_lst[4] + split_lst[7])
        arr3 = list(split_lst[2] + split_lst[5] + split_lst[8])
        if sum(arr1) != total or sum(arr2) != total or sum(arr3) != total:
            result = False 
    
    if result:
        # 3x3 조사(3)
        split_lst = []
        j = 0
        for i in range(3):
            j = 0
            for c in range(N):
                split_lst.append(row_lst[i+6][j:j+3])
                j += 3
                if j > 6:
                    break
        # 판별(3)
        arr1 = list(split_lst[0] + split_lst[3] + split_lst[6])
        arr2 = list(split_lst[1] + split_lst[4] + split_lst[7])
        arr3 = list(split_lst[2] + split_lst[5] + split_lst[8])
        if sum(arr1) != total or sum(arr2) != total or sum(arr3) != total:
            result = False 


    print('#{} {}'.format(T, int(result)))