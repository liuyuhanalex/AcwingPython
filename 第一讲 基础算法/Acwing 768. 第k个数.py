from typing import List


def quick_sort(arr: List[int], l: int, r: int, k):
    if l >= r:
        return arr[l]
    pivot = arr[(l + r) // 2]
    i, j = l - 1, r + 1
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
    if j - l + 1 >= k:
        return quick_sort(arr, l, j, k)
    else:
        return quick_sort(arr, j + 1, r, k-( j -l +1))


if __name__ == '__main__':
    n, k = [int(i) for i in input().split(' ')]
    arr = [int(i) for i in input().split(' ') if len(i) > 0]
    print(quick_sort(arr, 0, n - 1, k))