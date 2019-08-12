
import sys
sys.stdin = open('input.txt', 'r')

for T in range(1, int(input())+1):
    words = str(input())

    def Palindrome(words):
        return 1 if words == words[::-1] else 0

    print('#%d %s' % (T, Palindrome(words)))