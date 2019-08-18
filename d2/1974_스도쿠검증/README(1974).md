##  1974_스도쿠검증

### 1. 문제접근 과정

- 입력값 받기
- 가로줄, 세로줄 3X3 행렬 합이 각각 45인지 확인
- 한 번이라도 중복값이 나오면 **result는 0**이 된다

#### 1.1  행 탐색

```PYTHON
    total = 45
    result = True
    N = 9
    
    # 행조사
    row_lst = list(list(map(int, input().split())) for i in range(N))
    for r in row_lst:
        if sum(r) != 45:
            result = False 
            break
            
```

#### 1.2 열 탐색

```PYTHON
   if result:  # 만약 행 조사 해도 result 가 1이라면,
        #열조사
        col_lst = list(map(list, zip(*row_lst)))
        for c in col_lst:
            if sum(c) != 45:
                result = False 
                break
```



#### 1.3 3X3 탐색

```PYTHON
# 가로줄 3행씩 조사(0행 3줄, 3행 3줄, 6행 3줄)
    if result:  # 행, 열 조사해도 result가 1이라면..!
        k = 0  
        l = 0
        arr = []
        for i in range(k, k + 3):  # i는 행, k는 돌릴 범위
            for j in range(l, l + 3):  # j는 열, l은 돌릴 범위
                arr.append(row_lst[i][j])
        # print(arr)  # [4, 5, 7, 6, 3, 9, 7, 9, 3]
        if sum(arr) != total:
            result = False
        else:
            arr = []  # 다시 빈 리스트로 만들어주고
            k = 0  # k도 초기화하고
            l += 3  # 3~6열 조사
        if l > 9:  # l이 9를 넘어가면, 그냥 result 는 1이고 다음 단계로 넘어가자
            result = True
            k += 3  # 3행~6행 조사
```



### 2. 최종결과코드

```PYTHON
for T in range(1, int(input())+1):
    total = 45
    result = True
    N = 9
    
    row_lst = list(list(map(int, input().split())) for i in range(N))
    for r in row_lst:
        if sum(r) != 45:
            result = False 
            break
    
    if result:
        col_lst = list(map(list, zip(*row_lst)))
        for c in col_lst:
            if sum(c) != 45:
                result = False 
                break

    if result:
        k = 0
        l = 0
        arr = []
        for i in range(k, k + 3):
            for j in range(l, l + 3):
                arr.append(row_lst[i][j])
        if sum(arr) != total:
            result = False
        else:
            arr = []
            k = 0
            l += 3
        if l > 9:
            result = True
            k += 3

    print('#{} {}'.format(T, int(result)))
```

