import sys
sys.stdin = open('input.txt', 'r')

TC = int(input())
for t in range(1, TC+1):
    n = int(input())
    num_set = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}
    add_set = set()
    res = 0
    i = 0
    while add_set != num_set:
        i += 1
        res += 1
        if len(str(n*i)) == 1:
            add_set.add(str(n*i))
        else:
            for s in range(len(str(n*i))):
                add_set.add(str(n*i)[s])
    print('#{} {}'.format(t, res*n))

