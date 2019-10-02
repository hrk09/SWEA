# dfs 그래프 문제
import sys
sys.stdin = open('input.txt', 'r')

# dfs 함수만들기(stack, visited)
def dfs(start):
    stack.append(start)
    # 방문체크
    visited[start] = 1
    # 한 값씩 돌면서
    for i in range(1, node+1):
        if g[start][i] and not visited[i]:
            dfs(i)
    return stack

TC = int(input())
for t in range(1, 1+TC):
    # 정점, 간선수 받기
    node, edge = map(int, input().split())
    edges = []
    stack = [] # 결과
    visited = [0] * (node+1)
    cnt = 0

    # 간선수만큼 돌면서 edges 저장하기
    for e in range(edge):
        edges.extend(map(int, input().split()))
    # print(edges)

    # 양방향 그래프 만들기(node+1)
    g = [[0]*(node+1) for i in range(node+1)]
    # print(g)

    # edges의 짝수 인덱스는 시작점
    for i in range(0, len(edges), 2):
        # 정방향
        g[edges[i]][edges[i+1]] = 1
        # 역방향
        g[edges[i+1]][edges[i]] = 1
    # print(g)

    # 시작 값 설정(방문 안한 시작노드)
    for i in range(1, node+1):
        # i 가 방문 안했으면, dfs 실행 후, cnt += 1
        if not visited[i]:
            dfs(i)
            cnt += 1
    # print(cnt)

    print('#{} {}'.format(t, cnt))

