import sys
sys.stdin = open('input.txt', 'r')
# 분할정복
def who_win(a, b):
    if (cards[a-1] == 1 and cards[b-1] == 3) or (cards[a-1] == 1 and cards[b-1] == 1):
        return a
    elif (cards[a-1] == 2 and cards[b-1] == 1) or (cards[a-1] == 2 and cards[b-1] == 2):
        return a
    elif (cards[a-1] == 3 and cards[b-1] == 2) or (cards[a-1] == 3 and cards[b-1] == 3):
        return a
    return b

def match(s, e):
    # 시작지점과 끝점이 같아지면 종료
    if s == e:
        return s
    pre_match = match(s, (s+e)//2)
    post_match = match((s+e)//2+1, e)
    return who_win(pre_match, post_match)

TC = int(input())
for t in range(1, TC+1):
    n = int(input())
    cards = list(map(int, input().split()))
    s = 1
    e = n
    print('#{} {}'.format(t, match(s, e)))