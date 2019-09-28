import sys
sys.stdin = open('input', 'r')

def change(n, cnt=0):
    a = int(''.join(n))
    if empty_lst[cnt] > a:
        return 0
    empty_lst[cnt] = a
    # print(empty_lst[cnt])
    if cnt == c:
        return 0
    for i in range(len(n)):
        for j in range(i+1, len(n)):
            # 숫자 바꾸는 작업
            swap = n[:]
            swap[i], swap[j] = swap[j], swap[i]
            change(swap, cnt+1)

TC = int(input())
for t in range(1, TC+1):
    n, c = input().split()
    n = list(n)
    c = int(c)
    empty_lst = [0]*(c+1)
    change(n)
    print('#{} {}'.format(t, empty_lst[-1]))
