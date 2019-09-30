import sys
sys.stdin = open('input.txt', 'r')

def power_of_n(m):
    if m == 0:
        return 1
    else:
        return n * power_of_n(m-1)

for t in range(10):
    tc = int(input())
    n, m = map(int, input().split())
    print('#{} {}'.format(tc, power_of_n(m)))