# dfs로 풀기(본 이 문제는 bfs 문제이다)
import sys
sys.stdin = open('input.txt', 'r')

# dfs 함수 만들기
def dfs(start):
    # start 방문처리
    visited[start] = 1
    # next 노드 처리
    for next in range(1, node+1):
        if g[start][next] and not visited[next]:
            visited[next] = 1
            # 거리 측정(bfs 방식 거리가 0이면 하나 더한 값 추가하고,)
            if distance[next] == 0:
                distance[next] = distance[start] + 1
            # 거리가 0이 아니고 다음 거리가 start 거리보다 크면 1 더함(??)
            elif distance[next] != 0 and distance[next] > distance[start] + 1:
                distance[next] = distance[start] + 1
            # next로 dfs 함수 실행하고,
            dfs(next)
            # visited 는 다시 초기화해줌
            visited[next] = 0
    return distance

for t in range(1, 11):
    edge, start = map(int, input().split())
    edges = list(map(int, input().split()))
    # print(edges)
    node = max(edges)
    distance = [0] * (node+1)
    visited = [0] * (node+1)

    # 단방향 graph 만들기
    g = [[0]*(node+1) for i in range(node+1)]
    for i in range(0, len(edges), 2):
        g[edges[i]][edges[i+1]] = 1
    # print(g)

    dfs(start)


    # max_distance를 첫값으로 지정하고, 하나씩 돌리면서 max가 가장 긴 값의 idx를 찾는 것
    max_distance = distance[0]
    for i in range(1, len(distance)):
        # max dis 가 최대인 것 중에 가장 큰 값 찾는 것
        if max_distance <= distance[i]:
            max_distance = distance[i]
            res = i
    print('#{} {}'.format(t, res))

