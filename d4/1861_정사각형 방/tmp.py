# 완탐
import sys
sys.stdin = open('input.txt', 'r')

def probe(i, j, start):
    global res, cnt, dx, dy
    # base 케이스
    if i == n-1 and j == n-1:
        return 0
    else:
        for _ in range(4):
            # 상하좌우 이동
            tmp_i, tmp_j = i + dx[_], j + dy[_]
            if 0 <= tmp_i < n and 0 <= tmp_j < n and arr[i][j] +1 == arr[tmp_i][tmp_j]:
                cnt += 1
                probe(tmp_i, tmp_j, start + arr[tmp_i][tmp_j])

TC = int(input())
for t in range(1, TC+1):
    n = int(input())
    arr = [list(map(int, input().split())) for i in range(n)]
    res = []
    cnt = 0

    # 시작점 조사
    for i in range(n):
        for j in range(n):
            probe(i, j, arr[i][j])

    # 상하좌우조사
    dx = [1, -1, 0, 0]
    dy = [0, 0, -1, 1]

