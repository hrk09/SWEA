# bfs(dfs로 풀면 조건 제약이 많아져서 복잡해짐..)
import sys
sys.stdin = open('input.txt', 'r')

def bfs(start):
    q.append(start)
    visited[start] = 1
    while q:
        start = q.pop(0)
        for next in range(1, node+1):
            if g[start][next] and not visited[next]:
                q.append(next)
                visited[next] = 1
                distance[next] = distance[start] + 1
    return distance

for t in range(1, 11):
    edge, start = map(int, input().split())
    edges = list(map(int, input().split()))
    node = max(edges)

    # 단방향 g 만들기
    g = [[0]*(node+1) for i in range(node+1)]
    for i in range(0, len(edges), 2):
        g[edges[i]][edges[i+1]] = 1

    # bfs 작업
    q = []
    distance = [0]*(node+1)
    visited = [0]*(node+1)

    bfs(start)

    max_dis = max(distance)
    for idx in range(len(distance)):
        if distance[idx] >= max_dis:
            res = idx
            max_dis = distance[idx]
    print('#{} {}'.format(t, res))



