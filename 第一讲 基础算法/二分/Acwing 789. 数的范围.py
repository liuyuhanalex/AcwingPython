# 整数二分：有单调性的一定可以二分，可以二分的不一定具有单调性
# 1. mid = (l + r) / 2
from typing import List


def binary_search(arr: List[int], l: int, r: int, x: int):
    r_l, r_r = l, r
    while l < r:
        mid = (l + r) // 2
        if arr[mid] >= x:
            r = mid
        else:
            l = mid + 1
    left_limit = r
    l, r = r_l, r_r
    while l < r:
        mid = (l + r + 1) // 2
        if arr[mid] <= x:
            l = mid
        else:
            r = mid - 1
    right_limit = l
    if arr[left_limit] != x:
        return -1, -1
    return left_limit, right_limit


if __name__ == '__main__':
    n, q = [int(i) for i in input().split(' ')]
    arr = [int(i) for i in input().split(' ')]
    for i in range(q):
        q_i = int(input())
        l, r = binary_search(arr, 0, n-1, q_i)
        print(str(l) + ' ' + str(r))