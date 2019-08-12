words = str(input())


def Palindrome(words):
    if words == words[::-1]:
        return 1
    else:
        return 0

print(Palindrome(words))