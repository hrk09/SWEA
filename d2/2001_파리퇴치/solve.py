import sys
sys.stdin = open('input.txt', 'r')

TC = int(input())

for t in range(1, TC+1):
    N, M = map(int, input().split())
    N_arr = []

    for n in range(N):
        N_arr.append(list(map(int, input().split())))
    # print(N_arr)

    max_flies = 0
    # 시작점 찾기
    for i in range(N-M+1):
        for j in range(N-M+1):
            num_flies = 0
            for r in range(M):
                for c in range(M):
                    num_flies += N_arr[i+r][j+c]
            if num_flies > max_flies:
                max_flies = num_flies

    print('#{} {}'.format(t, max_flies))