# 190805

## 1979_어디에 단어가 들어갈 수 있을까



### 1.1. 문제풀이과정

- 행렬리스트 만들기(행, 열 따로)

- <u>행과 열을 **str타입**으로 만들기</u>

- str된 행,열을 **'1' * K**가 있는 만큼 count 하기
  
  

#### 1.1.1. 행렬 리스트를 str로 만들기

```python
# 행렬을 [[ ], [ ], [ ]], [[ ], [ ], [ ]]로 만들되, 각 행렬의 값을 str로 만들어야 한다.

row_list = [''.join(input().split()) for n in range(N)]  # 행 리스트를 str로 만들기
col_list = [''.join(i) for i in zip(*row_list)]  # 열 리스트를 str로 만들기(zip(*))

```

```python
# 출력결과

row_list = ['00111', '11110', '00100', '01111', '11101']
col_list = ['01001', '01011', '11111', '11010', '10011']

```



#### 1.1.2. 행과 열을 동시에 돌면서 행의 값과 열의 값에서 '1' * K 개수 세기

```python
row_list = [''.join(input().split()) for n in range(N)]  # 값을 str로 바꿈(행)
col_list = [''.join(i) for i in zip(*row_list)]  # 값을 str로 바꿈(열) zip(*)
cnt = 0  # '1' * K 를 세자

for l in (row_list, col_list):
    for i in l:
        cnt += i.split('0').count('1' * K)
        
# .join과 zip(*iterable) 개념        
```

```python
# 출력결과

['', '', '111']
['1111', '']
['', '', '1', '', '']
['', '1111']
['111', '1']
['', '1', '', '1']
['', '1', '11']
['11111']
['11', '1', '']
['1', '', '11']

```



### 2.1. 최종 결과코드

 ```python
import sys
sys.stdin = open('input.txt', 'r')

for T in range(1, int(input()) + 1): 
    N, K = map(int, input().split())
    row_list = [''.join(input().split()) for n in range(N)]  # 값을 str로 바꿈(행)
    col_list = [''.join(i) for i in zip(*row_list)]  # 값을 str로 바꿈(열) zip(*)
    cnt = 0

    for l in (row_list, col_list):
        for i in l:
            cnt += i.split('0').count('1' * K)

    print(f'#{T} {cnt}')
 ```

```python
# 출력결과

#1 2
#2 6
#3 6
#4 0
#5 14
#6 2
#7 45
#8 0
#9 98
#10 7
```



