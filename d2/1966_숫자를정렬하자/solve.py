import sys
sys.stdin = open('input.txt', 'r')

TC = int(input())
for t in range(1, TC+1):
    N = int(input())
    nums = list(map(int, input().split()))
    arr = sorted(nums)
    res = ''

    for i in range(N):
        res += str(arr[i]) + ' '

    print('#{} {}'.format(t, res))