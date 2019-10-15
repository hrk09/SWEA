import sys
sys.stdin = open('input.txt', 'r')

def dfs(start):
    global cnt
    stack.append(start)
    visited[start] = 1
    for i in range(1, n+1):
        if g[start][i] and not visited[i]:
            dfs(i)
    return stack


TC = int(input())
for t in range(1, TC+1):
    n, m = map(int, input().split())
    adj = list(map(int, input().split()))
    # print(adj)

    # 그래프 만들기
    g = [[0]*(n+1) for i in range(n+1)]

    for i in range(0, len(adj), 2):
        g[adj[i]][adj[i+1]] = 1
        g[adj[i+1]][adj[i]] = 1
    # print(g)

    cnt = 0
    visited = [0] * (n + 1)
    stack = []

    # 시작노드잡고 dfs 진행
    for i in range(0, 2*m, 2):
        print(dfs(adj[i]))
        cnt += 1
    print(cnt)


