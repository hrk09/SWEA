# dfs로 풀기(아직...) 아마 bfs로 풀어야 하는 것 같다...
import sys
sys.stdin = open('input.txt', 'r')

# dfs 함수 만들기
def dfs(start):
    stack.append(start)
    visited[start] = 1
    for i in range(1, node+1):
        if g[start][i] and not visited[i]:
            dfs(i)
    return stack

for t in range(1, 11):
    edge, start = map(int, input().split())
    # 노드 수
    node = 100
    stack = []
    visited = [0] * 101

    # edges 받기
    edges = list(map(int, input().split()))
    # print(edges)

    # 단방향 graph 만들기
    g = [[0]*(node+1) for i in range(node+1)]
    for i in range(0, len(edges), 2):
        g[edges[i]][edges[i+1]] = 1
    # print(g)

    print(dfs(start))

