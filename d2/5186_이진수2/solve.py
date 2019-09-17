import sys
sys.stdin = open('input.txt', 'r')

TC = int(input())

for t in range(1, TC+1):
    N = input()
    i = 1
    res = ''

    m, n = divmod(float(N), 0.5**i)
    res += str(int(m))
    # print(res)
    N = n  # 0.125

    while n:
        i += 1
        m, n = divmod(float(N), 0.5**i)
        res += str(int(m))
        N = n
    if len(res) > 15:
        print('#{} overflow'.format(t))
    else:
        print('#{} {}'.format(t, res))