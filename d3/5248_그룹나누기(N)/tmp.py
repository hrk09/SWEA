import sys
sys.stdin = open('input.txt', 'r')

TC = int(input())
for t in range(1, TC+1):
    n, m = map(int, input().split())
    adj = list(map(int, input().split()))
    group = []

    tmp = set()

    for start in range(0, 2*m, 2): # 시작노드
        end = start+1
        if not tmp:  # tmp에 아무것도 없으면, 첫 값 넣어줌
            tmp.add(adj[start]); tmp.add(adj[end])
        # tmp에 값이 있으면 연결노드 찾아서 연결해줌
        else:
            # 다음 start, end 값이 tmp에 있다면
            if (adj[start] or adj[end]) in tmp:
                tmp.add(adj[start]); tmp.add(adj[end])
            else:
                group.append(tmp)
                tmp = set()
                tmp.add(adj[start]);tmp.add(adj[end])
                group.append(tmp)
    print(group)