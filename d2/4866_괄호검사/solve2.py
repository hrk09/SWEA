for T in range(1, int(input()) + 1):
    words = input()
    stack = []  # 자릿수 정해주기
    result = True

    for w in words:
        if w == '(' or w == '{':
            stack.append(w)  # stack 에 ( or { 더하기
        if w == ')':
            if len(stack) == 0:
                result = False
                break
            elif stack[-1] == '(':
                stack.pop()
            else:
                result = False
                break
        elif w == '}':
            if len(stack) == 0:
                result = False
                break
            elif stack[-1] == '{':
                stack.pop()
            else:
                result = False
                break

    if len(stack) == 0 and result:
        result = True
    else:
        result = False

    print('#{} {}'.format(T, int(result)))