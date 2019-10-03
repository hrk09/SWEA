# bfs, 그래프
import sys
sys.stdin = open('input.txt', 'r')
# 5개만 맞는 이유....

def bfs(start):
    q.append(start)
    while q:
        n = q.pop(0)
        if n not in visited:
            visited.append(n)
            for i in range(v+1):
                if g[n][i] and i not in visited and i not in q:
                    q.append(i)
    return visited


for t in range(10):
    v, e = map(int, input().split())
    adj = list(map(int, input().split()))
    q = []
    res = []
    visited = []
    # 단방향 g 만들기
    g = [[0] * (v+1) for i in range(v+1)]
    for i in range(0, len(adj), 2):
        g[adj[i]][adj[i+1]] = 1
    adj_s = adj[::2]
    adj_e = adj[1::2]
    start = []
    # 시작점 세팅, v 중 끝에 없는 경우가 시작점
    for i in range(1, v+1):
        if i not in adj_e and i not in visited:
            start.append(i)
    for s in start:
        res = bfs(s)
        if len(res) == v:
            print('#{} {}'.format(t+1, ' '.join([str(i) for i in res])))
            break
            # res = bfs(i)
            # if len(res) == v:
            #     print('#{} {}'.format(t+1, ' '.join([str(i) for i in res])))
            #     break