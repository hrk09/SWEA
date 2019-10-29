import sys
sys.stdin = open('input.txt', 'r')

def is_palindrome(word):
    if word == word[::-1]:
        return True

for t in range(1, 11):
    l = int(input())
    arr = [input() for i in range(8)]
    arr_ = list(map(list, zip(*arr)))
    cnt = 0

    # 가로줄
    for i in range(8):
        for j in range(8-l+1):
            if is_palindrome(arr[i][j:j+l]):
                cnt += 1

    # 세로줄
    for i in range(8):
        for j in range(8-l+1):
            arr2 = ''.join(arr_[i][j:j+l])
            # print(arr2)
            if is_palindrome(arr2):
                cnt += 1

    print('#{} {}'.format(t, cnt))