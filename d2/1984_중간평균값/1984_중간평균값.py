import sys
sys.stdin = open('1984_input.txt', 'r')

TC = int(input())

for tc in range(1, TC+1):
    num_lst = list(map(int, input().split()))
    num_lst.sort()
    num_lst.pop(0) and num_lst.pop()
    print(num_lst)
    print('#{} {}'.format(tc, round(sum(num_lst)/len(num_lst))))