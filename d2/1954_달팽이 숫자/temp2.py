'''
4

1 2 3 4 
12 13 14 5 
11 16 15 6 
10 9 8 7 
'''
N = int(input())
matrix = [[0 for j in range(N)] for i in range(N)]

value = 1
i = 0
j = 0
k = 1

while N > 0:
    # A WALL(j증가)
    if k % 4 == 1:
        for j in range(N):
            matrix[i][j] = value # 0, 0
            value += 1
            if j > N:  # j가 N-1 넘어가면 break
                break
        k += 1
    # print(matrix, i, j, k) # 0, 3, 2

    # B WALL(i증가)
    if k % 4 == 2:
        for i in range(1, N): 
            matrix[i][j] = value
            value += 1
            if i > N:
                break
        k += 1
    # print(matrix, i, j, k) # 3, 3, 3

    # C WALL (j감소)
    if k % 4 == 3:
        for j in range(N-2, -1, -1):  # N = 4, 
            matrix[i][j] = value
            value += 1
            if j < 0:
                break
        k += 1
    # print(matrix, i, j, k)  # 3, 0, 4

    # D WALL(i감소)
    if k % 4 == 0:
        for i in range(N-2, -1, -1): 
            matrix[i][j] = value
            value += 1
            if i == 1:
                break
        k += 1
        N -= 2
        j += 1
    # print(matrix, i, j, k) # 1, 0, 4

print(matrix)
    
