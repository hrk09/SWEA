import sys
sys.stdin = open('input.txt', 'r')


def get_distance(P, Q):
    return abs(P[0]-Q[0]) + abs(P[1]-Q[1])


def travel(total, idx):
    global ans
    if total >= ans:
        return
    last_visit = customers[idx]
    if len(visited) == len(customers):
        ans = min(ans, total + get_distance(last_visit, home))
        return
    for i in range(len(customers)):
        if i in visited:
            continue
        visited.add(i)
        this_visit = customers[i]
        travel(total + get_distance(last_visit, this_visit), i)
        visited.remove(i)


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    points = list(map(int, input().split()))
    office = (points[0], points[1])
    home = (points[2], points[3])
    customers = [office]
    for x in range(4, 2*N+4, 2):
        customers.append(tuple(points[x:x+2]))
    ans = float('INF')
    visited = set((0,))
    travel(0, 0)
    print('#{} {}'.format(tc, ans))