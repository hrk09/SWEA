N = 3
val_list = list(val for val in range(1, N*N + 1))

i = 0
j = 0
idx = 0
arr = [[0 for j in range(N)] for i in range(N)]

# 기본 matrix 만들기
for i in range(N):
    for j in range(N):
        arr[i][j] = val_list[idx]
        idx += 1
# print(arr) # [[1, 2, 3], [4, 5, 6], [7, 8, 9]]