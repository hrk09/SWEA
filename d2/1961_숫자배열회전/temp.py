import sys
sys.stdin = open('input.txt', 'r')
'''
10
3
1 2 3
4 5 6
7 8 9

output
741 987 369 
852 654 258 
963 321 147 
'''

for T in range(1, int(input())+1):
    N = int(input())

    arr = list(list(map(int, input().split(' '))) for n in range(N))
    # print(value)  # [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    result_1 = []
    result_2 = []
    result_3 = []


    # 90도 회전
    reversed_1 = list(map(list, zip(*arr)))
    for i in reversed_1:
        result_1.append(list(reversed(i)))
    # print(result_1)  # [[7, 4, 1], [8, 5, 2], [9, 6, 3]]

    # 180도 회전
    reversed_2 = list(map(list, zip(*result_1)))
    for i in reversed_2:
        result_2.append(list(reversed(i)))
    # print(result_2)  # [[9, 8, 7], [6, 5, 4], [3, 2, 1]]

    # 270도 회전
    reversed_3 = list(map(list, zip(*result_2)))
    for i in reversed_3:
        result_3.append(list(reversed(i)))
    # print(result_3)  # [[3, 6, 9], [2, 5, 8], [1, 4, 7]]

    print('#%d' % T)
    for i in range(N):
        print(''.join(map(str, result_1[i])), ''.join(map(str, result_2[i])), ''.join(map(str, result_3[i])))