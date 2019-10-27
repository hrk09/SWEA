import sys
sys.stdin = open('input.txt', 'r')

TC = int(input())
for t in range(1, TC+1):
    nums = input().split()
    max_num, min_num = 0, 987654321
    for i in range(1, len(nums)):
        tmp = 0
        for j in range(len(nums[i])):
            tmp += int(nums[i][j])
        if tmp > max_num:
            max_num = tmp
        elif tmp < min_num:
            min_num = tmp
    print('#{} {} {}'.format(t, max_num, min_num))