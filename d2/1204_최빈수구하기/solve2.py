# 시간이 많이걸리는 코드
import sys
sys.stdin = open('input.txt', 'r')

TC = int(input())
for t in range(TC):
    n = int(input())
    scores = list(map(int, input().split()))
    max_mode = 0
    cnt = 0

    # 예외경우 처리 해주기..
    for s in scores:
        if s != max_mode:
            if scores.count(s) > cnt:
                max_mode = s
                cnt = scores.count(s)
            elif scores.count(s) == cnt:
                if max_mode < s:
                    max_mode = s
    print('#{} {}'.format(n, max_mode))