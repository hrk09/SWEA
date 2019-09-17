import sys
sys.stdin = open('input.txt', 'r')

TC = int(input())

for tc in range(1, TC+1):
    c, t = map(int, input().split())
    cw = list(map(int, input().split()))
    tw = list(map(int, input().split()))

    cw1 = sorted(cw)  # 정렬
    tw1 = sorted(tw)
    weight = []  # 중량 넣을 리스트

    if c <= t:  # 역순으로 돌리면서
        for i in range(c-1, -1, -1):
            for j in range(t-1, -1, -1):
                if cw1[i] <= tw1[j]:  # 트럭이 컨테이너보다 크거나 같으면
                    weight.append(cw1[i])  # weight에 값을 추가하고
                    tw1[j] = 0  # 해당 인덱스 트럭값을 0으로 둔다
                    break
    else:
        for j in range(t-1, -1, -1):
            for i in range(c-1, -1, -1):
                if cw1[i] <= tw1[j]:
                    weight.append(cw1[i])
                    tw1[j] = 0
                    break

    print('#{} {}'.format(tc, sum(weight)))




