import sys
sys.stdin = open('input.txt', 'r')

TC = int(input())
for t in range(1, TC+1):
    n = int(input())
    money = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    cnt = [0]*8

    for i in range(len(money)):
        if n // money[i] >= 1:
            cnt[i] = n // money[i]
            # 금액 갱신
            n -= cnt[i] * money[i]
    print('#{}\n{}'.format(t, ' '.join([str(c) for c in cnt])))
