import sys
sys.stdin = open('input.txt', 'r')

for T in range(int(input())):  # 테스트케이스
    N, k = map(int,input().split())  # N x N, k개 단어

    for i in range(N):  # N까지 하나씩
        row_i = list(map(int, input().split()))
    # print(row_i)
