import sys
sys.stdin = open('input.txt', 'rt', encoding='UTF8')

for T in range(10):
    tc = int(input())
    fi = input()
    words = input()
    cnt = 0

    for i in range(len(words)):
        if words[i] == fi[0]:
            if words[i:i+len(fi)] == fi:
                cnt += 1
    print('#{} {}'.format(tc, cnt))
