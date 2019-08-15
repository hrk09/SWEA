import sys
sys.stdin = open('input.txt', 'r')

for T in range(1, int(input())+1):
    N = int(input())

    arr = list(list(map(int, input().split(' '))) for n in range(N))
    # print(value)  # [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    # 90도 회전
    reversed_1 = list(map(list, zip(*arr)))

    # 180도 회전
    reversed_2 = list(map(list, zip(*reversed_1)))

    # 270도 회전
    reversed_3 = list(map(list, zip(*reversed_2)))

    print('#%d' % T)
    for i in range(N):
        print(' '.join(map(str, reversed_1[i])), ' '.join(map(str, reversed_2[i])), ' '.join(map(str, reversed_3[i])))