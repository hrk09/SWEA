import sys
sys.stdin = open('input.txt', 'r')
# 가로 세로 겹치면 안됨
# dfs로 풀어서 값 최소면 저장하기
def dfs(i):
    global tmp_sum, min_sum
    # tmp_sum이 중간에 min_sum 그냥 넘어버리면, min_sum은 계속 min_sum으로 감
    # 불필요한 계산 작업 방지
    if min_sum < tmp_sum:
        return min_sum
    # dfs(3)// i==3 일 때,
    if i == n:
        if tmp_sum < min_sum:
            min_sum = tmp_sum
            return min_sum
    # 0 행일 때, j를 n까지 돌리면서
    for j in range(n):
        # 방문 안했으면, 방문처리하기
        if not visited[j]:
            visited[j] = 1
            tmp_sum += arr[i][j]
            print('1', tmp_sum)
            # 다음 행으로 넘어감// i + 1 이 3이면 dfs(i=3)이니, i = n이면 판단 후 종료
            dfs(i+1)
            # dfs 다 끝나면, j 행 visited 0으로 바꿔서 앞으로 못가게 하고, tmp_sum에서 마지막값빼기
            visited[j] = 0
            tmp_sum -= arr[i][j]
            print('2', tmp_sum)


TC = int(input())
for t in range(1):
    n = int(input())
    arr = [list(map(int, input().split())) for i in range(n)]
    tmp_sum = 0
    min_sum = 9999999
    visited = [0]*n

    # 시작값 잡기(0행부터 돌리기)
    dfs(0)
    print('#{} {}'.format(t, min_sum))

