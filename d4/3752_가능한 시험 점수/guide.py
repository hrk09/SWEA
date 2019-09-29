import sys
sys.stdin = open('input.txt', 'r')

TC = int(input())
for t in range(1, TC+1):
    N = int(input())
    scores = list(map(int, input().split()))
    res = {0} # 0은 무조건

    # scores 한 값씩 돌면서
    for i in scores:
        for j in list(res):
            res.add(i+j)
    print('#{} {}'.format(t, len(res)))