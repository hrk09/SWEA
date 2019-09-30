import sys
sys.stdin = open('input.txt', 'r')

def is_powerset(lst):
    x = len(lst)
    res =[]
    cnt = 0
    for i in range(1 << x):
        res.append([lst[j] for j in range(x) if i & (1 << j)])
    # return res
    for r in res:
        if len(r) == n and sum(r) == k:
           cnt += 1
    return cnt


TC = int(input())
for t in range(1, TC+1):
    n, k = map(int, input().split())
    a = []

    for i in range(1, 13):
        a.append(i)

    # 합이 k이고 부분집합 개수가 n인 것 찾기
    print('#{} {}'.format(t, is_powerset(a)))

