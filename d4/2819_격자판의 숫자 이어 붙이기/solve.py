import sys
sys.stdin = open('input.txt', 'r')
# 완탐

def probe(i, j, s):
    global res
    # 길이가 7개면 set에 넣음(중복제거)
    if len(s) == 7:
        return res.add(s)
    else:
        for _ in range(4):
            # 상하좌우 이동
            tmp_i, tmp_j = i + dx[_], j + dy[_]
            # 벽에 닿지 않는 조건
            if 0 <= tmp_i < 4 and 0 <= tmp_j < 4:
                probe(tmp_i, tmp_j, s + arr[tmp_i][tmp_j])

TC = int(input())
for t in range(1, TC+1):
    arr = [list(input().split()) for i in range(4)]
    res = set()
    # 상하좌우
    dx = [1, -1, 0, 0]
    dy = [0, 0, -1, 1]
    # 시작점 설정
    for i in range(4):
        for j in range(4):
            probe(i, j, arr[i][j])

    print('#{} {}'.format(t, len(res)))