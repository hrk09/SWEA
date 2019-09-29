import sys
sys.stdin = open('input.txt', 'r')
'''
0점은 항상 받을 수 있는 점수
새로운 점수 받을 때마다 더해주고, 이전에 가능한 점수들 + 새로받은 점수 더해
가능한 점수 체크
'''
def res(scores):
    res = {0}
    for i in scores:
        for j in list(res):
            res.add(i+j)
    return len(res)

TC = int(input())
for t in range(1, TC+1):
    N = int(input())
    scores = list(map(int, input().split()))
    print('#{} {}'.format(t, res(scores)))