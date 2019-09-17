import sys
sys.stdin = open('input.txt', 'r')

TC = int(input())
for t in range(1, TC+1):
    N, nums = input().split()

    letter = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
    result = ''

    for n in range(int(N)):
        if nums[n] not in letter.keys():
            ori_binary = bin(int(nums[n]))
            binary = ori_binary[2:]
            if len(binary) != 4:
                res = '0'*(4-len(binary)) + binary
                result += res
            else:
                result += binary

        else:
            ori_binary = bin(letter.get(nums[n]))
            binary = ori_binary[2:]
            if len(binary) != 4:
                res = '0'*(4-len(binary)) + binary
                result += res
            else:
                result += binary

    print('#{} {}'.format(t, result))