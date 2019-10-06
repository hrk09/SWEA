# 경로가 존재하는 지 여부 조사하는 문제 (dfs)
import sys
sys.stdin = open('input.txt', 'r')

# 옮긴 인덱스가 범위 내 있고, 갈 수 있는 지 확인하는 작업
def is_safe(x, y):
    if 0 <= x < n and 0 <= y < n and (miro[x][y] == '0' or miro[x][y] == '3'):
        return True

# dfs 함수 생성
def dfs(x, y):
    global res
    # 3 나오면 그냥 res 는 1
    if miro[x][y] == '3':
        res = 1
        return res
    # 그렇지 않으면, 다음 dfs 작업 실행함
    else:
        visited.append((x, y))  # 4 3
        # 상하좌우 조사
        for _ in range(4):
            nx = x + dx[_]
            ny = y + dy[_]
            # 새로 지정한 nx와 ny 가 실행 조건 만족하고, 방문한 적이 없으니까
            if is_safe(nx, ny) and (nx, ny) not in visited:
                # dfs 실행 가능함
                dfs(nx, ny)
    return res

TC = int(input())
for t in range(1, TC+1):
    n = int(input())
    res = 0
    # 그래프 받기
    miro = [list(input()) for i in range(n)]

    # 상하좌우조사
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    visited = []

    # 출발점
    for x in range(n):
        for y in range(n):
            if miro[x][y] == '2':
                sx, sy = x, y
    print('#{} {}'.format(t, dfs(sx, sy)))