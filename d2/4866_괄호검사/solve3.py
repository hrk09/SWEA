import sys
sys.stdin = open('input.txt', 'r')

TC = int(input())
for t in range(1, TC+1):
    words = input()
    stack = []

    for w in words:
        # 여는 괄호가 올 경우 => stack에 저장
        if w == "(" or w == "{":
            stack.append(w)
        # 닫는 괄호가 온다면, stack 상태에 따라 달라짐.
        elif w == ")" or w == "}":
            # stack이 빈 경우 => 처음부터 닫는 괄호가 오는 경우
            if not stack:
                # stack에 한 값을 넣어야 나중에 결과값 출력에서 0으로 나옴
                # 이 처리를 안하면, 나중에 stack 없을 때 1 출력하는데 여기서
                # 걸릴 수 있음..!!!
                stack = [w]
                break
            # stack 마지막에 저장된 괄호와 일치하지 않는 경우
            elif (w == "}" and stack[-1] != "{") or (w == ")" and stack[-1] != "("):
                stack = [w]
                break
            # stack에 저장된 괄호와 일치하는 닫는 괄호가 오는 경우
            else:
                stack.pop()

    if not stack:
        print('#{} 1'.format(t))
    else:
        print(f'#{t} 0')