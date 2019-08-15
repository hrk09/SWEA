import sys
sys.stdin = open('input.txt', 'r')

for T in range(1, int(input())+1):
    times = list(map(int, input().split(' ')))

    hour = sum(times[0: 4: 2])
    minute = sum(times[1: 4: 2])

    def SumTime(hour, minute):
        if minute >= 60:
            minute -= 60
            hour += 1
        if hour >= 12:
            hour -= 12
        return '{} {}'.format(hour, minute)
    
    print('#{} {}'.format(T, SumTime(hour, minute)))