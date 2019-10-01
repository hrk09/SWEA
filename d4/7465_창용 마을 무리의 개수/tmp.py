# dfs 문제
import sys
sys.stdin = open('input.txt', 'r')

def dfs(graph, start):
    visited = []
    stack = [start]

    while stack:
        v = stack.pop()
        if v not in visited:
            visited.append(v)
            if v in graph:
                tmp = list(set(graph[v]) - set(visited))
                stack += tmp
    return visited


TC = int(input())
for t in range(1, TC+1):
    people, node = map(int, input().split())
    graph = {}
    tmp = []

    # graph dict 만들기
    for n in range(node):
        n1, n2 = map(int, input().split())
        if n1 not in graph:
            graph[n1] = [n2]
        # graph[n1]에 n2가 없다면,
        elif n2 not in graph[n1]:
            graph[n1].append(n2)
    print(graph)

    for k in range(1, people+1):
        tmp += [dfs(graph, k)]

