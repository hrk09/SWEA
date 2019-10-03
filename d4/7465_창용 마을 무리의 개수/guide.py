import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for t in range(1, T + 1):
    people, node = map(int, input().split())
    arr = [[] for _ in range(people+1)]
    visited = [1] * (people + 1)
    cnt = 0
    for _ in range(node):
        a, b = map(int, input().split())
        arr[a].append(b)
        arr[b].append(a)

    tmp = []
    for i in range(1, people+1):
        if not visited[i]:
            continue
        tmp.append(i)
        visited[i] = 0
        while tmp:
            q = tmp.pop(0)
            for j in arr[q]:
                if visited[j]:
                    tmp.append(j)
                    visited[j] = 0
        cnt += 1
    print('#{} {}'.format(t, cnt))