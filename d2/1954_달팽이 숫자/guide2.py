# import sys
# sys.stdin = open('input.txt', 'r')
 
for T in range(1, int(input())+1):
    n = int(input())  
    for y in range(0, n):
        for x in range(0, n):
            p = min(x, y, n-x-1, n-y-1)
            if x >= y:
                q = x+y - 2*p
            else:
                q = (n-1 - 2*p)*4 - (x+y - 2*p)
            q += 4 * (p*n - (p*p)) + 1
            print("{:3d}".format(q), end="")
        print()
