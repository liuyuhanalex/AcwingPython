# 归并排序 -> 分治
# 1. 确定分界点 mid = (l+r)//2 2. 递归排序left, right 3.归并 - 合二为一
# 时间复杂度  n*logn
from typing import List


def merge_sort(arr: List[int], l: int, r: int):
    if l >= r:
        return
    mid = (l + r) // 2
    merge_sort(arr, l, mid), merge_sort(arr, mid+1, r)
    i, j, tmp = l, mid+1, []
    while i <= mid and j <= r:
        if arr[i] <= arr[j]:
            tmp.append(arr[i])
            i += 1
        else:
            tmp.append(arr[j])
            j += 1
    if i <= mid:
        tmp += arr[i: mid+1]
    if j <= r:
        tmp += arr[j: r+1]
    arr[l: r+1] = tmp


if __name__ == '__main__':
    n = int(input())
    arr = [int(i) for i in input().split(' ')]
    merge_sort(arr, 0, n - 1)
    for i in arr:
        print(i, end=' ')