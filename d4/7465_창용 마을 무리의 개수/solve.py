import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for t in range(1, T+1):
    people, node = map(int, input().split())
    # graph 받기
    graph = [[] for _ in range(people+1)]
    # 방문여부 확인
    visited = [1]*(people+1)
    cnt = 0

    # graph 완성
    for _ in range(node):
        n1, n2 = map(int, input().split())
        graph[n1].append(n2)
        graph[n2].append(n1)
    # print(graph)

    stack = []
    for i in range(1, people+1):
        # 방문 했으면 그냥 넘어가기
        if not visited[i]:
            continue
        stack.append(i)
        visited[i] = 0
        # stack이 빌때까지
        while stack:
            start = stack.pop(0)
            # 시작값 리스트 값 돌면서
            for j in graph[start]:
                # 방문한 적이 없으면 stack 에 하나 추가하고 방문처리
                if visited[j]:
                    stack.append(j)
                    visited[j] = 0
        # 끝나면 cnt +1 하기
        cnt += 1
    print('#{} {}'.format(t, cnt))