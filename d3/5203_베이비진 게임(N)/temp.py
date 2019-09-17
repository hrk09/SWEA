import sys
sys.stdin = open('input.txt', 'r')

TC = int(input())

for t in range(2):
    card = list(map(int, input().split()))
    # print(card)
    p1 = card[::2]
    print('P1', p1)  # [9, 5, 5, 1, 4, 2]
    p2 = card[1::2]
    print('P2', p2)  # [9, 6, 6, 1, 2, 1]


def triplet(l):

def run(l):
    for l1 in range(6):
        for l2 in range(l1, 6)