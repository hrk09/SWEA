import sys
sys.stdin = open('input.txt', 'r')

prime_nums = [2, 3, 5, 7, 11]
(a, b, c, d, e) = (0, 0, 0, 0, 0)
print(prime_nums[1])

def prime_number(N):
    for prime_num in prime_nums:
        while print_num <= N:
            if N % prime_num == 0:
                a += 1
                N = N / prime_num
            else:
                prime_num += 1


              N % prime_num == 0:
            a += 1
            N = N / prime_num
        if N % prime_num != 0:
            prime_nums[]    

case_num = int(range(-1))

print(f'#{num}'enumerate(a, b, c, d, e)