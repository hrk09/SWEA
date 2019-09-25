import sys
sys.stdin = open('input.txt', 'r')

TC = int(input())
for t in range(1, TC+1):
    N = int(input())
    k = []
    res = 0

    for i in range(1, N+1):
        k += [i]

    for i in range(N):
        if i % 2: # 홀수
            res -= k[i]
        else:
            res += k[i]

    print('#{} {}'.format(t, res))


