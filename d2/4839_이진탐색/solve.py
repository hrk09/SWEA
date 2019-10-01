import sys
sys.stdin = open('input.txt', 'r')

# 함수 식
def binarysearch(find):
    start = 1
    end = total
    cnt = 0
    while start <= end:
        cnt += 1
        mid = (start + end) // 2
        if mid == find:
            return cnt
        elif mid < find:
            start = mid
        else:
            end = mid
    return cnt


TC = int(input())
for t in range(1, TC+1):
    total, a, b = map(int, input().split())
    if binarysearch(a) > binarysearch(b):
        print('#{} B'.format(t))
    elif binarysearch(a) == binarysearch(b):
        print('#{} 0'.format(t))
    else:
        print('#{} A'.format(t))