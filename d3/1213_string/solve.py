import sys
sys.stdin = open('input.txt', 'rt', encoding='UTF8')

for T in range(10):
    tc = int(input())
    find = input()
    n_find = len(find)
    words = input()
    n_words = len(words)
    cnt = 0

    # 슬라이싱으로 풀기
    for i in range(n_words-n_find+1):
        if words[i:i+n_find] == find:
            cnt += 1
    print('#{} {}'.format(tc, cnt))
