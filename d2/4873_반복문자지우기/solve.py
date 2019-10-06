'''
3
ABCCB
NNNASBBSNV
UKJWHGGHNFTCRRCTWLALX

#1 1
#2 4
#3 11
'''
TC = int(input())
for t in range(1, TC+1):
    words = input()
    stack = []

    for i in range(len(words)):
        # 스택이 비면 그냥 그 값 stack 넣음
        if not stack:
            stack.append(words[i])
        else:
            if words[i] == stack[-1]:
                stack.pop(-1)
            else:
                stack.append(words[i])
    print('#{} {}'.format(t, len(stack)))