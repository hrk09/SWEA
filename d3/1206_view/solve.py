import sys
sys.stdin = open('input.txt', 'r')



for t in range(1, 11):
    N = int(input())
    building = list(map(int, input().split()))

    def solve(x):
        cnt = 0
        for a in range(2, N-2):
            result = building[a] - max(building[a-2], building[a-1], building[a+1], building[a+2])
            if result > 0:
                cnt += result
        return cnt

    print('#{} {}'.format(t, solve(building)))