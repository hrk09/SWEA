import sys
sys.stdin = open('input', 'r')


TC = int(input())
for t in range(1, TC+1):
    n = int(input())
    arr = [int(x) for x in input().split()]
    cnt = 0

    def merge_sort(arr):
        if len(arr) <= 1:
            return arr

        mid = len(arr)//2
        left = arr[:mid]
        right = arr[mid:]

        left_1 = merge_sort(left)
        right_1 = merge_sort(right)
        return merge(left_1, right_1)


    def merge(left, right):
        global cnt
        i = 0
        j = 0
        sorted_lst = []
        if left[-1] > right[-1]:
            cnt += 1

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                sorted_lst.append(left[i])
                i += 1
            else:
                sorted_lst.append(right[j])
                j += 1

        while i < len(left):
            sorted_lst.append(left[i])
            i += 1

        while j < len(right):
            sorted_lst.append(right[j])
            j += 1

        return sorted_lst


    print('#{} {} {}'.format(t, merge_sort(arr)[n//2], cnt))