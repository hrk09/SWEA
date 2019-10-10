import sys
sys.stdin = open('input.txt', 'r')

# 큐

TC = int(input())
for t in range(1, TC+1):
    n, m = map(int, input().split())
    nums = list(input().split())
    for i in range(m):
        tmp = nums.pop(0)
        nums.append(tmp)

    print('#{} {}'.format(t, nums[0]))