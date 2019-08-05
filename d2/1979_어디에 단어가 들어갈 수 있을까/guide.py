import sys
sys.stdin = open('input.txt', 'r')

for T in range(int(input())): 
    N, K = map(int,input().split())
    b = [''.join(input().split()) for n in range(N)]  # 가로줄 리스트
    t = [''.join(i) for i in zip(*b)]  # 세로줄 리스트
    r = 0
    for c in (b,t):
        for l in c:
            r += l.split('0').count('1'*K)
    print(r)
    # print(f'#{T+1} {r}')