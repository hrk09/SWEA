import sys
sys.stdin = open('input.txt', 'r')

def prime(n):
    i = 0
    for i in range(5):
        while not n % prime_n[i]:
            res[i] += 1
            n //= prime_n[i]
    return res

TC = int(input())
for t in range(1, TC+1):
    n = int(input())
    prime_n = [2, 3, 5, 7, 11]
    res = [0, 0, 0, 0, 0]
    print('#{} {}'.format(t, ' '.join([str(i) for i in prime(n)])))