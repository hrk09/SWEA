import sys
sys.stdin = open('input.txt', 'r')

# 재귀함수
def bin_recurr(start, end, find):
    global cnt
    if start > end:
        return cnt
    else:
        cnt += 1
        mid = (start+end) // 2
        if find == mid:
            return cnt
        elif find > mid:
            return bin_recurr(mid, end, find)
        else:
            return bin_recurr(start, mid, find)


TC = int(input())
for t in range(1, TC+1):
    end, a, b = map(int, input().split())
    cnt = 0
    cnt_a = bin_recurr(1, end, a)
    # 초기화 안 하면, cnt_a가 cnt에 들어가게 됨
    cnt = 0
    cnt_b = bin_recurr(1, end, b)

    if cnt_a > cnt_b:
        print('#{} B'.format(t))
    elif cnt_a < cnt_b:
        print('#{} A'.format(t))
    else:
        print('#{} 0'.format(t))