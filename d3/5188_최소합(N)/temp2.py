import sys
sys.stdin = open('input', 'r')

TC = int(input())

for t in range(1):
    N = int(input())

    arr = [list(map(int, input().split())) for n in range(N)]
    temp = [arr[0][0]]

    # while i != N-1 and j != N-1:
    for i in range(N-1):
        print(i)