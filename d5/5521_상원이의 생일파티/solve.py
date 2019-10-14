import sys
sys.stdin = open('input.txt', 'r')

# bfs 신경쓸 필요 없이 1행, 1열만 신경쓰면 됨(1행, 1열은 상원이), 1열에서 상원이 친구의 친한친구만 파악해서 1로 갱신

TC = int(input())
for t in range(1, TC+1):
    node, edge = map(int, input().split())

    edges = []
    for e in range(edge):
        edges.extend(map(int, input().split()))
    print('e', edges)

    g = [[0] * (node+1) for i in range(node+1)]
    for i in range(0, len(edges), 2):
        g[edges[i]][edges[i+1]] = 1
        g[edges[i+1]][edges[i]] = 1
    res = [0] * (node+1)
    print('g', g)
    # print(g[1])  # 상원이 친구
    idx =[]

    for i in range(1, node+1):
        if g[1][i]:
            # 상원이 친구 등록
            res[i] = 1
            idx += [i]

    for i in idx:
        for j in range(1, node+1):
            if g[i][j]:
                # print(j)
                res[j] = 1

    # 1,1 은 상원이 지니까 0으로 만들어주기
    res[1] = 0
    print(res)
    print('#{} {}'.format(t, sum(res)))



