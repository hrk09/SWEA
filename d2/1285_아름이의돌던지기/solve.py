import sys
sys.stdin = open('input.txt', 'r')

for T in range(1, int(input()) + 1):
    people = int(input())
    distance = list(map(int, input().split(' ')))
    abs_lst = []  # 절댓값 리스트

    for d in range(len(distance)):
        abs_lst.append(abs(distance[d]))
        result = min(abs_lst)
    
    cnt = abs_lst.count(result)
    
    print('#{} {} {}'.format(T, result, cnt))