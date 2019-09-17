import sys
sys.stdin = open('input.txt', 'r')

TC = int(input())

for tc in range(1, TC+1):
    c, t = map(int, input().split())
    cw = list(map(int, input().split()))
    tw = list(map(int, input().split()))

    cw1 = sorted(cw)
    tw1 = sorted(tw)
    weight = []

    if c <= t:  # 작은 수만큼 돌리는데
        for i in range(c-1, -1, -1):
            for j in range(t-1, -1, -1):
                if cw1[i] <= tw1[j]:
                    weight.append(cw1[i])
                    tw1[j] = 0
                    break
    else:
        for j in range(t-1, -1, -1):
            for i in range(c-1, -1, -1):
                if cw1[i] <= tw1[j]:
                    weight.append(cw1[i])
                    tw1[j] = 0
                    break

    print('#{} {}'.format(tc, sum(weight)))




