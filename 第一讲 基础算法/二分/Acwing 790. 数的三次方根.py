def binary_search(num):
    l, r = -10000, 10000
    while r - l > 1e-8:
        mid = (l + r) / 2
        if mid**3 >= num:
            r = mid
        else:
            l = mid
    return l


if __name__ == '__main__':
    num = float(input())
    print('%06f'% binary_search(num))
