import sys
sys.stdin = open('input.txt', 'r')

for T in range(1, int(input())+1):
    times = list(map(int, input().split(' ')))

    for i in range(len(times)):
        if i % 2:  # i % 2가 True(1)이면 minute에 담기
            minute += times[i]
        else:
            hour += times[i]

    if minute >= 60:
        hour += 1
        minute -= 60
    if hour >= 12:
        hour -= 12 
    
    print('#{} {} {}'.format(T, hour, minute))