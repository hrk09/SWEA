
snail = [[0] * 5 for _ in range(5)]  # 숫자를 넣으려고 하는 리스트
# 배열이 뭐냐? 변수 여러개
X = 0  # 내가 숫자를 넣으려고 하는 좌표(인덱스) => 행
Y = 0  # 열
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
d = 0

def iswall(x, y):
    if x < 0 or x >= 5: return True
    if y < 0 or y >= 5: return True
    if snail[x][y] != 0: return True
    return False

for i in range(1, 26):
    snail[X][Y] = i
    X += dx[d]
    Y += dy[d]
    if iswall(X + dx[d], Y + dy[d]):  # wall이면 방향 전환
        d = (d + 1) % 4

for ii in range(5):
    p = ''
    for jj in range(5):
        p += str(snail[ii][jj]) + ' '
    print(p)