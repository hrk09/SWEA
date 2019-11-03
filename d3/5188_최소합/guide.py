import itertools
import sys
sys.stdin = open('input', 'r')

T = int(input())
for test_case in range(1, T + 1):
    size = int(input())
    ltlt = list()
    for i in range(size):
        ltlt.append(list(input().split(" ")))
    solList = 100000
    def findPath(i,j,result):
        global solList
        if result > solList:
            return
        if i>=size or j>=size:
            return
        elif i==size-1 and j==size-1:
            result+=int(ltlt[i][j])
            if solList > result:
                solList = result
            return
        else:
            result+=int(ltlt[i][j])
            findPath(i+1,j,result)
            findPath(i,j+1,result)
    findPath(0,0,0)
    print("#{} {}".format(test_case,solList))
