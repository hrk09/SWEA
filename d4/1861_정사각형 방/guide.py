import sys
sys.stdin = open('input.txt', 'r')

def dfs(x, y):
    max = 0
    for i in range(4):
        tx = x + dx[i]
        ty = y + dy[i]

        if tx < 0 or ty < 0 or tx == N or ty == N: continue
        if data[x][y] + 1 == data[tx][ty]:
            ret = dfs(tx, ty)
            if ret > max:
                max = ret

    return max + 1


T = int(input())
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
MAXN = 1000

for tc in range(1, T + 1):
    N = int(input())
    data = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        data[i] = list(map(int, input().split()))

    ans = 987654321
    max = 0

    for x in range(N):
        for y in range(N):
            ret = dfs(x, y)
            if ret > max:
                max = ret
                ans = data[x][y]
            elif ret == max and ans > data[x][y]:  # 같으면 작은걸로
                ans = data[x][y]

    print("#{} {} {}".format(tc, ans, max))