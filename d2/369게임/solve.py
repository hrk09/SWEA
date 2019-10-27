'''
10
1 2 - 4 5 - 7 8 - 10
'''

n = input()
clap = ['3', '6', '9']

for i in range(1, int(n)+1):
    res = ''
    cnt = 0  # '-' 개수 찍기 위한 것
    for j in str(i):
        if j in clap:
            cnt += 1
    if cnt:  # cnt가 하나라도 있으면,
        res += '-'*cnt
    else:
        res = str(i)
    print(res, end=' ')
