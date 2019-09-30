import sys
sys.stdin = open('input.txt', 'r')


def distance(s, e):
    return abs(s[0]-e[0]) + abs(s[1]-e[1])


def travel(total, idx):
    global ans
    if total >= ans:
        return
    last_visit = customers[idx]
    if len(visited) == len(customers):
        ans = min(ans, total + distance(last_visit, house))
        return
    for i in range(len(customers)):
        if i in visited:
            continue
        visited.add(i)
        this_visit = customers[i]
        travel(total + distance(last_visit, this_visit), i)
        visited.remove(i)

TC = int(input())
for t in range(1, TC + 1):
    v = int(input())
    lst = list(map(int, input().split()))
    location = []

    # 좌표 location 만들기
    for i in range(0, (v + 2) * 2, 2):
        location.append((lst[i], lst[i + 1]))

    company = location[0]
    house = location[1]
    customers = location[2:]
    customers.insert(0, company)
    # print(customers)

    ans = float('INF')
    visited = set((0,))
    travel(0, 0)
    print('#{} {}'.format(t, ans))
    




