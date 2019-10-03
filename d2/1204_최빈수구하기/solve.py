import sys
sys.stdin = open('input.txt', 'r')

TC = int(input())
for t in range(TC):
    n = int(input())
    scores = list(map(int, input().split()))
    # 중복제거해야 나중에 조사할 때, 시간이 확 줄어든다..
    scores_set = set()
    max_mode = 0
    cnt = 0

    for s in scores:
        scores_set.add(s)

    # 예외경우 처리 해주기..
    for s in scores_set:
        if scores.count(s) > cnt:
            max_mode = s
            cnt = scores.count(s)
        elif scores.count(s) == cnt:
            if max_mode < s:
                max_mode = s
    print('#{} {}'.format(n, max_mode))
