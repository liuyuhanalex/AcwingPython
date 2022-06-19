# 1. 左半边内部的逆序对数量: merge_sort(L, mid)
# 2. 右半边内部的逆序对数量: merge_sort(mid + 1, R)
# 3. 在归并过程中每次输出 qj 的时候加上一个 mid - i + 1
from typing import List


def merge_sort(arr: List[int], l: int, r: int):
    if l >= r:
        return 0
    mid = (l + r) // 2
    res = merge_sort(arr, l, mid) + merge_sort(arr, mid+1, r)
    i, j, tmp = l, mid + 1, []
    while i <= mid and j <= r:
        if arr[i] <= arr[j]:
            tmp.append(arr[i])
            i += 1
        else:
            tmp.append(arr[j])
            res += mid - i + 1
            j += 1
    if i <= mid:
        tmp += arr[i: mid+1]
    if j <= r:
        tmp += arr[j: r+1]
    arr[l: r+1] = tmp
    return res


if __name__ == '__main__':
    n = int(input())
    arr = [int(i) for i in input().split(' ')]
    print(merge_sort(arr, 0, n - 1))
