import sys
sys.stdin = open('input.txt', 'r')

for t in range(1, 11):
    v, e = map(int, input().split())
    mymap = [[0]*(v+1) for _ in range(v+1)]
    adj = list(map(int, input().split()))

    for i in range(0, len(adj), 2):
        # mymap 끝값의 시작값에 저장
        mymap[adj[i+1]][adj[i]] = 1

    result = []
    while True:
        if len(result) == v:
            break

        # 시작점 찾기
        start_set = []
        for start in range(1, len(mymap)):
            if 1 not in mymap[start] and start not in result:
                start_set.append(start)
        # print(start_set)

        # 시작점 set 에서 하나씩 돌면서
        for start in start_set:
            result.append(start)
            for end in range(v+1):
                mymap[end][start] = 0

    print('#{} {}'.format(t, ' '.join([str(i) for i in result])))