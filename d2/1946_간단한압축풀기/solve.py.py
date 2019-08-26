import sys
sys.stdin = open('1946_input.txt', 'r')

TC = int(input())
for tc in range(1, TC+1):
    N = int(input())
    alpha_str = ''
    for n in range(N):
        ci, ki = input().split()
        alpha_str += ci * int(ki)
    result = ''
    # 10개씩 나눠서 출력
    k = 0
    print('#{}'.format(tc))
    for a in range(len(alpha_str)//10):  # 3줄
        while k < len(alpha_str):
            print(alpha_str[k:k+10])
            k += 10