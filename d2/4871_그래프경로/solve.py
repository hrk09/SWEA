import sys
sys.stdin = open('input.txt', 'r')
# dfs 문제
def dfs(s):
    global res
    stack.append(s)
    visited[s] = 1
    for i in range(1, v+1):
        if G[s][i] and not visited[i]:
            dfs(i)
    if g in stack:
        return 1
    else:
        return 0


TC = int(input())
for t in range(1, TC+1):
    v, e = map(int, input().split())
    edges =[]
    for i in range(e):
        edges.extend(list(map(int, input().split())))
    s, g = map(int, input().split())
    stack = []
    visited = [0]*(v+1)
    res = 0

    # 단방향 그래프 만들기
    G = [[0]*(v+1) for i in range(v+1)]
    for i in range(0, len(edges), 2):
        G[edges[i]][edges[i+1]] = 1
    # print(G)

    print('#{} {}'.format(t, dfs(s)))