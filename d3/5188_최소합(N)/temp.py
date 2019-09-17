import sys

sys.stdin = open('input', 'r')

TC = int(input())

for t in range(1):
    N = int(input())

    arr = [list(map(int, input().split())) for n in range(N)]
    temp = []
    res = 0

    temp.append(arr[0][0])  # 시작점 넣기
    # print(temp)

    for i in range(N-1):
        if i != N-1:
            temp.append([i][j+1])
        else:
        for j in range(N-1):
            if j == N-1:
                break
                print(i, j)


    # # NxN 행렬의 경우, 도착까지 2N-1 번 반복작업함
    # for r in range(2*N-1):
    #     temp.append(arr[0][0])  # 시작점 넣기
    #     for i in range(N-1):
    #         for j in range(N-1):
    #             # 벽에 부딪히면
    #             if i == N-2:
    #                 temp.append(arr[i][j+1])
    #             elif j == N-2:
    #                 temp.append(arr[i+1][j])
    #             else:  # 벽이 아니면
    #                 if temp[i+1][j] > temp[i][j+1]:
    #                     temp.append(arr[i][j+1])
    #                 elif temp[i+1][j] < temp[i][j+1]:
    #                     temp.append(arr[i+1][j])
    # if sum(temp) < res:
    #     res = sum(temp)
    #
    # print(res)
