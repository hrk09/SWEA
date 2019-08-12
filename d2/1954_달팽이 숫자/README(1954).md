# 190809

## 1954_달팽이숫자



### 1.1. 문제풀이과정

- N x N 행렬리스트 만들기

  - arr에 배열할 숫자 리스트를 미리 만들기 (예) 4x4면 1~16까지 num_list에 담는다 

- N이 짝수일 때와 홀수일 때로 나눠서 생각하기

  - 홀수인 경우, 정 가운뎃값이 추가됨

- 각 행렬을 4면으로 나눠서 반복문 돌리기
  
  

#### 1.1.1. 행렬과 행렬에 배열할 숫자 리스트 만들기

```python
# N * N 행렬 만들기(arr)
N = int(input())
    arr = [[0 for j in range(N)] for i in range(N)]
    num_list = list(range(1, N ** 2 + 1))
```



#### 1.1.2. N이 짝수인 경우와, 홀수인 경우로 나누기

```python
    N = int(input())
    arr = [[0 for j in range(N)] for i in range(N)]
    num_list = list(range(1, N ** 2 + 1))  # n x n 숫자를 list에 넣음

    idx= 0  # num_list를 도는 index값   
    c = 0  
 
    if N % 2 == 0:
        k = int(N / 2)  # N이 4이면, 4X4, 2X2만 넣으면 됨
    else:
        k = int((N - 1) / 2)  # N이 5이면, 5X5, 3X3하고 정가운뎃값하나 들어감
```



#### 1.1.2. 각 행렬을 A면, B면, C면, D면으로 나눠서 반복문 돌리기

- range 변수 설정 주의

```PYTHON
for c in range(k):
    for j in range(c, N - c):  # A면(j 증가)
        arr[c][j] = num_list[idx]
        idx += 1
    for i in range(c + 1, N - c):  # B면(i 증가)
        arr[i][N - c - 1] = num_list[idx]
        idx += 1
    for j in range(N - 2 - c, c - 1, -1):  # C면(j 감소)
        arr[N - c - 1][j] = num_list[idx]
        idx += 1
    for i in range(N - 2 - c, c, -1):  # D면(i 감소)
        arr[i][c] = num_list[idx]
        idx += 1
    c += 1  # 4면 다 돌면 1 증가시키고 맨 위 for문 돌리기
```

#### 1.1.3.  N이 홀수인 경우, 정가운뎃값이 들어가므로 따로 조건을 설정해야함

```PYTHON
if N % 2 == 1:
   arr[k][k] = num_list[idx] # 가운데 값 = num_list의 최종 idx 값
```



### 2.1. 최종 결과코드

 ```python
import sys
sys.stdin = open('input.txt', 'r')

for T in range(1, int(input())+1):
    N = int(input())
    arr = [[0 for j in range(N)] for i in range(N)]
    num_list = list(range(1, N ** 2 + 1))

    idx = 0
    c = 0
 
    if N % 2 == 0:
        k = int(N / 2)
    else:
        k = int((N - 1) / 2)
 
    for c in range(k):
        for j in range(c, N - c):
            arr[c][j] = num_list[idx]
            idx += 1
        for i in range(c + 1, N - c):
            arr[i][N - c-1] = num_list[idx]
            idx += 1
        for j in range(N - 2 - c, c - 1, -1):
            arr[N - c-1][j] = num_list[idx]
            idx += 1
        for i in range(N - 2 - c, c, -1):
            arr[i][c] = num_list[idx]
            idx += 1
        c += 1
 
    if N % 2 == 1:
        arr[k][k] = num_list[idx]

    print(f'#{T}')
    for i in range(N):
        print(' '.join(map(str,arr[i])))  # 한 열씩 문자열로 출력
 ```

```python
# 출력결과

#1
1    
#2   
1 2  
4 3  
#3   
1 2 3
8 9 4
7 6 5
#4
1 2 3 4
12 13 14 5
11 16 15 6
10 9 8 7
#5
1 2 3 4 5
16 17 18 19 6
15 24 25 20 7
14 23 22 21 8
13 12 11 10 9
#6
1 2 3 4 5 6
20 21 22 23 24 7
19 32 33 34 25 8
18 31 36 35 26 9
17 30 29 28 27 10
16 15 14 13 12 11
#7
1 2 3 4 5 6 7
24 25 26 27 28 29 8
23 40 41 42 43 30 9
22 39 48 49 44 31 10
21 38 47 46 45 32 11
20 37 36 35 34 33 12
19 18 17 16 15 14 13
#8
1 2 3 4 5 6 7 8
28 29 30 31 32 33 34 9
27 48 49 50 51 52 35 10
26 47 60 61 62 53 36 11
25 46 59 64 63 54 37 12
24 45 58 57 56 55 38 13
23 44 43 42 41 40 39 14
22 21 20 19 18 17 16 15
#9
1 2 3 4 5 6 7 8 9
32 33 34 35 36 37 38 39 10
31 56 57 58 59 60 61 40 11
30 55 72 73 74 75 62 41 12
29 54 71 80 81 76 63 42 13
28 53 70 79 78 77 64 43 14
27 52 69 68 67 66 65 44 15
26 51 50 49 48 47 46 45 16
25 24 23 22 21 20 19 18 17
#10
1 2 3 4 5 6 7 8 9 10
36 37 38 39 40 41 42 43 44 11
35 64 65 66 67 68 69 70 45 12
34 63 84 85 86 87 88 71 46 13
33 62 83 96 97 98 89 72 47 14
32 61 82 95 100 99 90 73 48 15
31 60 81 94 93 92 91 74 49 16
30 59 80 79 78 77 76 75 50 17
29 58 57 56 55 54 53 52 51 18
28 27 26 25 24 23 22 21 20 19
```



