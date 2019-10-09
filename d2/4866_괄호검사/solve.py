import sys
sys.stdin = open('input.txt', 'r')

TC = int(input())
for t in range(1, TC+1):
    words = input()
    stack = []
    res = 1
    # 한 글자씩 돌면서
    for w in words:
        # 여는괄호로 시작하면, 일단 stack에 넣는다.
        if w == '(' or w == '{':
            stack.append(w)
        # 그러다가 닫는 괄호를 만나면,
        if w == ')':
            if not stack:
                res = 0
                break
            else:
                if stack[-1] == '(':
                    stack.pop()
                else:  # ')'나오는 경우,
                    res = 0
                    break
        if w == '}':
            if not stack:
                res = 0
                break
            else:
                if stack[-1] == '{':
                    stack.pop()
                else:
                    res = 0
                    break

    if not stack and res:
        print('#{} 1'.format(t))
    else:
        print('#{} 0'.format(t))