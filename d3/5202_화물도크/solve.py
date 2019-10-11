import sys
sys.stdin = open('input.txt', 'r')

# 도착시간이 가장 짧은 것 기준으로 찾으면 됨
TC = int(input())

for t in range(1, TC+1):
    N = int(input())
    l = []

    for n in range(N):
        s, e = map(int, input().split())
        l.append((e, s))  # 도착시간을 맨 앞으로 해서 저장

    l2 = sorted(l)
    # print(l2)

    res = set()  # tc에 중복되는 값이 들어오는 경우가 있음
    res.add(l2[0])
    min_e = l2[0][0]

    for i in range(1, N):
        if min_e <= l2[i][1]:
            res.add(l2[i])
            min_e = l2[i][0]
    # print(sorted(res))

    print('#{} {}'.format(t, len(res)))




