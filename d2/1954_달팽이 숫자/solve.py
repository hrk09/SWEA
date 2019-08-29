import sys
sys.stdin = open('input.txt', 'r')

for T in range(1, int(input())+1):
    N = int(input())
    arr = [[0 for j in range(N)] for i in range(N)]
    num_list = list(range(1, N ** 2 + 1))  # n x n 숫자를 list에 넣음

    idx = 0
    # 짝수 k = n / 2
    # 홀수 k = (n - 1) / 2
 
    if N % 2 == 0:  # N x N 이 짝수
        H = int(N / 2)  # 4면 2번만 넣으면 됨
    else:
        H = int((N - 1) / 2)  # 3이면 N-1 가운데 값
 
    for h in range(H):  # 4일 때 2번 돌리면 됨
        # 열증가(행 그대로)
        for j in range(h, N - h):
            arr[h][j] = num_list[idx]
            idx += 1
        # 행증가(열 그대로)
        for i in range(h + 1, N - h):
            arr[i][N - h-1] = num_list[idx]
            idx += 1
        # 열감소(행 그대로)
        for j in range(N - 2 - h, h - 1, -1):
            arr[N - h-1][j] = num_list[idx]
            idx += 1
        # 행감소(열 그대로)
        for i in range(N - 2 - h, h, -1):
            arr[i][h] = num_list[idx]
            idx += 1
 
    if N % 2 == 1:  # N x N 이 홀수
        arr[H][H] = num_list[idx]  # 가운데 값 = num_list idx의 끝값

    print('#{}'.format(T))
    for i in range(N):
        print(' '.join(map(str,arr[i])))