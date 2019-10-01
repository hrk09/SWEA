import sys
sys.stdin = open('input.txt', 'r')

def cnt_powerset(arr):
    x = len(arr)
    res = []
    cnt = 0
    for i in range(1<<x):
        sub_set = []
        for j in range(x):
            if i & (1<<j):
                sub_set.append(arr[j])
        if len(sub_set) == n and sum(sub_set) == k:
            cnt += 1
    return cnt

TC = int(input())
for t in range(1, TC+1):
    arr = [i for i in range(1, 13)]
    # print(arr)
    n, k = map(int, input().split())
    print('#{} {}'.format(t, cnt_powerset(arr)))