import sys
sys.stdin = open('input.txt', 'r')

TC = int(input())
for t in range(1, TC+1):
    n = int(input())
    commands = [list(map(int, input().split())) for _ in range(n)]
    # print(commands)
    v = 0
    d = 0

    for command in commands:
        if command[0] == 1:
            v += command[1]
            d += v
        elif command[0] == 2:
            if v < command[1]:
                v = 0
            else:
                v -= command[1]
                d += v
        # 현재속도 유지면, 그냥 그 거리만큼 +하면 됨
        elif not command[0]:
            d += v
    print('#{} {}'.format(t, d))