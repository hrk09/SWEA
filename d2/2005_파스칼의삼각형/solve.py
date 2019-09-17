import sys
sys.stdin = open('input.txt', 'r')

def pascal(n):
    if n == 0:
        return []
    elif n == 1:
        return [[1]]
    else:
        new = [1]
        result = pascal(n-1)
        last = result[-1]
        for i in range(len(last)-1):
            new.append(last[i] + last[i+1])
        new += [1]
        result.append(new)
    return result

TC = int(input())
for t in range(1, TC+1):
    N = int(input())
    print('#{}'.format(t))

    for n in range(N):
        result = pascal(N)[n]
        s = ''
        for r in range(len(result)):
            s += str(result[r]) + ' '
        print(s)