import sys
sys.stdin = open('input.txt', 'r')

def distance(s, e):
    return abs(s[0]-e[0]) + abs(s[1]-e[1])

TC = int(input())
for t in range(1):
    v = int(input())
    lst = list(map(int, input().split()))
    location = []

    # 좌표 location 만들기
    for i in range(0, (v+2)*2, 2):
        location.append((lst[i], lst[i+1]))
    # print(location)

    company = location.pop(0)
    house = location.pop(0)
    customer = location
    # print(customer)

    # 회사, 집, 고객 좌표, 최소거리
    s = company
    res = 0
    order = []
    min_dis = distance(s, customer[0])

    while v != 1:
        # 최소 거리 찾기
        for c in customer:
            if min_dis > distance(s, c):
                min_dis = distance(s, c)
                order.append(c)
                customer.remove(c)
        res += min_dis
        s = order[-1]
        v -= 1
    print(res)







