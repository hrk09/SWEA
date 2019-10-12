import sys
sys.stdin = open('input.txt', 'r')

TC = int(input())
for t in range(1, TC+1):
    p, q, r, s, w = map(int, input().split())
    a = p*w
    if w <= r:
        b = q
    else:
        b = q+(w-r)*s
    if a < b:
        print('#{} {}'.format(t, a))
    else:
        print('#{} {}'.format(t, b))
