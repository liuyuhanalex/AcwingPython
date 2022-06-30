if __name__ == '__main__':
    n, m = [int(i) for i in input().split(' ')]
    arr = [int(i) for i in input().split(' ')]
    prefix, prefix_list = 0,  []
    for i in range(n):
        prefix += arr[i]
        prefix_list.append(prefix)
    for j in range(m):
        l, r = [int(i)-1 for i in input().split(' ')]
        print(prefix_list[r] - prefix_list[l] + arr[l])
