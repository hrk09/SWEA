# 제한시간초과
import sys
sys.stdin = open('input.txt', 'r')

def powerset(s):
    x = len(s)
    res = set()
    for i in range(1 << x):
        p = sum([s[j] for j in range(x) if (i & (1 << j))])
        res.add(p)
    return res

TC = int(input())
for t in range(1, TC+1):
    N = int(input())
    scores = list(map(int, input().split()))
    print('#{} {}'.format(t, len(powerset(scores))))
