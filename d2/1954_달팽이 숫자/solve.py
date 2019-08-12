import sys
sys.stdin = open('input.txt', 'r')

for T in range(1, int(input())+1):
    N = int(input())
    arr = [[0 for j in range(N)] for i in range(N)]
    num_list = list(range(1, N ** 2 + 1))  # n x n 숫자를 list에 넣음

    idx = 0
    c = 0
    # 짝수 k = n / 2
    # 홀수 k = (n - 1) / 2
 
    if N % 2 == 0:  # N x N 이 짝수
        k = int(N / 2)  # 4면 2번만 넣으면 됨
    else:
        k = int((N - 1) / 2)  # 3이면 N-1 가운데 값
 
    for c in range(k):
        for j in range(c, N - c):
            arr[c][j] = num_list[idx]
            idx += 1
        for i in range(c + 1, N - c):
            arr[i][N - c-1] = num_list[idx]
            idx += 1
        for j in range(N - 2 - c, c - 1, -1):
            arr[N - c-1][j] = num_list[idx]
            idx += 1
        for i in range(N - 2 - c, c, -1):
            arr[i][c] = num_list[idx]
            idx += 1
        c += 1
 
    if N % 2 == 1:  # N x N 이 홀수
        arr[k][k] = num_list[idx]  # 가운데 값

    print(f'#{T}')
    for i in range(N):
        print(' '.join(map(str,arr[i])))