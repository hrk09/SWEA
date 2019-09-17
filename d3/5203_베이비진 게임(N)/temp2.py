import sys
sys.stdin = open('input.txt', 'r')

def is_run(l):
    for i in range(4):
        if 2 * l[i+1][0] == l[i][0] + l[i+2][0]:
            return max(l[i][1], l[i+1][1], l[i+2][1])

def is_triple(l):
    for i in range(4):
        if l[i] == l[i+1] == l[i+2]:
            return max(l[i][1], l[i+1][1], l[i+2][1])

TC = int(input())
for t in range(1, TC + 1):
    card = list(map(int, input().split()))

    ## p1
    p1 = card[::2]
    p11 = []
    for i in range(6):
        p11.append((p1[i], i))  # 카드번호, idx(뽑는순서)
    p111 = sorted(p11)

    d1 = []
    if is_run(p111):
        d1.append(is_run(p111))
    elif is_triple(p111):
        d1.append(is_triple(p111))
    else:
        d1 += [0]
    # print(d1)

    ## p2
    p2 = card[1::2]
    p22 = []
    for i in range(6):
        p22.append((p2[i], i))
    p222 = sorted(p22)

    d2 = []
    if is_run(p222):
        d2.append(is_run(p222))
    elif is_triple(p222):
        d2.append(is_triple(p222))
    else:
        d2 += [0]
    # print(d2)

    if 0 in d1 and 0 in d2:
        print('#{} 0'.format(t))
    elif 0 in d1 and 0 not in d2:
        print('#{} 2'.format(t))
    elif 0 not in d1 and 0 in d2:
        print('#{} 1'.format(t))
    else:
        if min(d1) < min(d2):
            print('#{} 1'.format(t))
        elif min(d1) > min(d2):
            print('#{} 2'.format(t))
        else:
            print('#{} 0'.format(t))