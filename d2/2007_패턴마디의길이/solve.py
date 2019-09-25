import sys
sys.stdin = open('input.txt', 'r')

TC = int(input())
for t in range(1, TC+1):
    w = list(input())
    w1 = w[0]
    w2 = w[1]
    w3 = w[2]

    for i in range(3, 28):
        if w[i] == w1:
            if w[i+1] == w2 and w[i+2] == w3:
                idx = i
                break

    print('#{} {}'.format(t, idx))
