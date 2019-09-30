# dfs 문제(깊이우선탐색)
import sys
sys.stdin = open('input.txt', 'r')


def distance(x, y):
    return abs(x[0]-y[0]) + abs(x[1]-y[1])

def dfs(cnt, i):
    global ans
    if cnt >= ans:
        return
    last_visit = location[i]
    else:


TC = int(input())
for t in range(1):
    v = int(input())
    lst = list(map(int, input().split()))
    location = []
    order = []
    res = 0

    # 좌표 location 만들기
    for i in range(0, (v+2)*2, 2):
        location.append((lst[i], lst[i+1]))

    company = location.pop(0)
    house = location.pop(0)
    customer = location
    ans = float('inf')
    visited = [0] * v

    start = company
    min_dis = distance(start, customer[0])

    for i in range(v, 0, -1):
        if len(order) != v:
            for c in customer:
                if min_dis > distance(start, c):
                    min_dis = distance(start, c)
                    end = c
            res += min_dis
            start = end
            customer.remove(start)




