# 快速排序 -> 分治
# 1.确定分界点  2.调整区间  3.递归处理左右两段
from typing import List


def quick_sort(arr: List[int], l: int, r: int):
    if l >= r:
        return
    pivot, i, j = arr[(l+r) // 2], l-1, r+1
    while i < j:
        while True:
            i += 1
            if arr[i] >= pivot:
                break
        while True:
            j -= 1
            if arr[j] <= pivot:
                break
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
    quick_sort(arr, l, j)
    quick_sort(arr, j+1, r)


if __name__ == '__main__':
    n = int(input())
    arr = [int(i) for i in input().split(' ') if len(i) > 0]
    quick_sort(arr, 0, n - 1)
    print(' '.join([str(i) for i in arr]))
