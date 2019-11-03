import sys
sys.stdin = open('input', 'r')

def is_safe(x, y):
    if 0 <= x < n and 0 <= y < n:
        return True

def dfs(x, y):
    global tmp_sum, min_sum
    # 이 과정이 들어가야 제한시간 초과가 뜨지 않음..ㅠ
    if min_sum < tmp_sum:  # 중간에 tmp가 이미 있던 min_sum보다 커지면 굳2 할 필요가 없으니 끝냄
        return min_sum
    if x == n-1 and y == n-1:
        min_sum = tmp_sum
        return min_sum
    for _ in range(2):
        nx = x + dx[_]
        ny = y + dy[_]
        if is_safe(nx, ny) and (nx, ny) not in visited:
            visited.append((nx, ny))
            tmp_sum += arr[nx][ny]
            dfs(nx, ny)
            # 방문 경로 초기화하는 작업
            visited.remove((nx, ny))
            tmp_sum -= arr[nx][ny]
    return min_sum

TC = int(input())

for t in range(1, TC+1):
    n = int(input())
    arr = [list(map(int, input().split())) for i in range(n)]
    visited = []
    tmp_sum, min_sum = arr[0][0], 99999999

    # 우, 하
    dx = [0, 1]  # 행
    dy = [1, 0]  # 열

    dfs(0, 0)
    print('#{} {}'.format(t, min_sum))