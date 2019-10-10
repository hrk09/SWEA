# bfs 문제
import sys
sys.stdin = open('input.txt', 'r')


def bfs(x, y):
    global min_dis
    q.append((x, y))
    visited.append((x, y))
    while q:
        x, y = q.pop(0)
        # dx, dy 돌면서 조사하기
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < n and 0 <= ny < n and (miro[nx][ny] == '0' or miro[nx][ny] == '3') and (nx, ny) not in visited:
                q.append((nx, ny))
                visited.append((nx, ny))
                # x, y = nx, ny 노갱신, 이미 갱신된건 q에 들어가서 x, y가 됨
                distance_arr[nx][ny] += distance_arr[x][y] + 1
                if miro[nx][ny] == '3':
                    min_dis = distance_arr[nx][ny] - 1
                    return min_dis

TC = int(input())
for t in range(1, TC+1):
    n = int(input())
    miro = [list(input()) for i in range(n)]
    min_dis = 0
    q = []
    visited = []
    # bfs에서 거리 계산할 때, distance matrix 만들어서 각각 거리 +1 씩 하는 작업
    distance_arr = [[0]*n for i in range(n)]
    for i in range(n):
        for j in range(n):
            if miro[i][j] == '2':
                sx, sy = i, j

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    bfs(sx, sy)

    print('#{} {}'.format(t, min_dis))