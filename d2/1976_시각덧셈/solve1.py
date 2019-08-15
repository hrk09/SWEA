import sys
sys.stdin = open('input.txt', 'r')

'''
3
3 17 1 39
'''


for T in range(1, int(input())+1):
    times = list(map(int, input().split(' ')))

    hour = []
    minute = []

    for i in range(len(times)):
        if i % 2:  # i % 2가 True(1)이면 minute에 담기
            minute.append(times[i])
        else:
            hour.append(times[i])

    if sum(minute) >= 60:
        result_minute = sum(minute) - 60
        result_hour = sum(hour) + 1
        if result_hour > 12:
            result_hour -= 12 
    else:
        result_minute = sum(minute)
        result_hour = sum(hour)
        if result_hour > 12:
            result_hour -= 12
    
    print('#{} {} {}'.format(T, result_hour, result_minute))