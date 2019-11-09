import sys
sys.stdin = open('sample_input.txt', 'r')

TC = int(input())

for t in range(1, TC+1):
    # N 숫자개수, C 바꾸는 횟수, I 인덱스 결과 출력
    N, C, I = map(int, input().split())
    numbers = list(map(int, input().split()))

    for c in range(C):
        idx, add_num = map(int, input().split())
        result = numbers[:idx] + [add_num] + numbers[idx:]
        # numbers 갱신작업
        numbers = result

    print('#{} {}'.format(t, result[I]))