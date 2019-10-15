import sys
sys.stdin = open('input.txt', 'r')

TC = int(input())
for t in range(1, TC+1):
    n, m = map(int, input().split())

    a_word = []
    b_word = []
    for i in range(n):
        a_word.append(input())
    for j in range(m):
        b_word.append(input())

    cnt = 0
    if n >= m:
        for i in range(m):
            if b_word[i] in a_word:
                cnt += 1
    else:
        for i in range(n):
            if a_word[i] in b_word:
                cnt += 1
    print('#{} {}'.format(t, cnt))