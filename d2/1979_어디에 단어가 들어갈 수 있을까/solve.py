import sys
sys.stdin = open('input.txt', 'r')

for T in range(1, int(input()) + 1): 
    N, K = map(int, input().split())
    row_list = [''.join(input().split()) for n in range(N)]  # 값을 str로 바꿈(행)
    col_list = [''.join(i) for i in zip(*row_list)]  # 값을 str로 바꿈(열) zip(*)
    cnt = 0

    for l in (row_list, col_list):
        for i in l:
            cnt += i.split('0').count('1' * K)
            '''
            ['', '', '111']
            ['1111', '']
            ['', '', '1', '', '']
            ['', '1111']
            ['111', '1']
            ['', '1', '', '1']
            ['', '1', '11']
            ['11111']
            ['11', '1', '']
            ['1', '', '11']
            '''
    print(f'#{T} {cnt}')