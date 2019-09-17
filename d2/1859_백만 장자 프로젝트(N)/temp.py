'''
3
10 7 6
3
3 5 9
5
1 1 3 1 2
'''

N = int(input())
lst = list(map(int, input().split()))
buy = []

for l in lst:
    if lst[-1] > l:
